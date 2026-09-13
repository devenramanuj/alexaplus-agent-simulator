import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# Initialize Gemini Client (GEMINI_API_KEY environment variable will be picked automatically)
client = genai.Client()

# In-memory storage for simulated tasks/reminders
SIMULATED_MEMORY = {
    "reminders": [],
    "notes": []
}

def add_reminder(task: str, time_str: str = "soon") -> str:
    """Tool: Adds a reminder or scheduled task to the assistant memory."""
    entry = {"task": task, "time": time_str, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")}
    SIMULATED_MEMORY["reminders"].append(entry)
    return f"Reminder successfully set: '{task}' for '{time_str}'."

def get_reminders() -> str:
    """Tool: Lists all active reminders."""
    if not SIMULATED_MEMORY["reminders"]:
        return "No active reminders found."
    return json.dumps(SIMULATED_MEMORY["reminders"])

def get_device_status(device_name: str) -> str:
    """Tool: Checks the status of simulated smart home devices."""
    statuses = {
        "living room light": "OFF",
        "thermostat": "72°F / Auto",
        "front door": "Locked",
        "kitchen plug": "ON"
    }
    normalized = device_name.strip().lower()
    for key, val in statuses.items():
        if key in normalized:
            return f"The status of {key} is {val}."
    return f"Device '{device_name}' is connected and operating normally."

# Register simulated agentic tools for Alexa+ experience
tools_list = [add_reminder, get_reminders, get_device_status]

SYSTEM_INSTRUCTION = """
You are Alexa+, a sophisticated, proactive, and friendly AI assistant and agent simulator.
You have access to simulated agentic tool calls (reminders, smart home status, memory).
When the user asks you to set a reminder, control a device, or check status, use your tools.
Provide concise, helpful, and natural responses suitable for a smart assistant display and voice output.
CRITICAL: You must ALWAYS respond strictly in the English language, regardless of the input language.
"""


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_prompt = data.get("message", "").strip()

    if not user_prompt:
        return jsonify({"error": "Empty message"}), 400

    try:
        # Strictly using gemini-2.5-flash
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                tools=tools_list,
                temperature=0.7,
            ),
        )
        
        reply_text = response.text or "I processed your request, but have no text response."
        return jsonify({
            "response": reply_text,
            "memory": SIMULATED_MEMORY
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
