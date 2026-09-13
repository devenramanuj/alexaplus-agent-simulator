# Alexa+ Agent Simulator

An open-source, web-based simulation of the **Alexa+** agentic assistant experience, built for the Amazon Developer Hackathon (Alexa+ Track).

## 🚀 Overview
The project demonstrates autonomous agentic capabilities within a browser interface:
- Multi-turn conversational reasoning.
- Simulated Model Context Protocol (MCP) tool execution (reminders, smart home status queries, and agent state memory).
- Clean, responsive dashboard designed for smart displays.

## 🛠️ Tech Stack
- **Backend:** Python 3, Flask
- **LLM Engine:** Gemini 2.5 Flash (`google-genai` SDK)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript

## ⚙️ Quickstart / Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/alexaplus-agent-simulator.git](https://github.com/YOUR_USERNAME/alexaplus-agent-simulator.git)
   cd alexaplus-agent-simulator

Install dependencies:
pip install -r requirements.txt

Set your API Key:
	export GEMINI_API_KEY="your-gemini-api-key"


Run the server:
	python app.py


Open http://localhost:5000 in your browser.
