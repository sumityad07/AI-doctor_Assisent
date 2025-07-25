# 🧠 AI Doctor Assistant

An intelligent AI-powered web application that lets users **speak their symptoms** and **upload a medical image** (e.g., X-ray), then returns a real-time diagnosis — both as **text** and **doctor's voice**.

> 🔬 Built for educational purposes, this tool simulates how AI can assist in first-level diagnosis.

---

## 🩺 Features

- 🎙️ Voice-to-text symptom transcription using Whisper
- 🖼️ Medical image analysis using LLM (LLaMA/Groq)
- 🗣️ Doctor-like responses converted into realistic voice (via ElevenLabs)
- 🌐 Fully interactive web UI built with Gradio
- 🔐 Secure with `.env` for API key management

---

## 🚀 How to Run Locally

> **Make sure you have Python 3.10+ and Git installed.**

### 1. Clone the Repository

bash
git clone https://github.com/sumityad07/AI-doctor_Assisent.git
cd AI-doctor_Assisent
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Environment Variables
Create a .env file in the root folder with:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key
ELEVEN_API_KEY=your_elevenlabs_api_key
5. Run the App
bash
Copy
Edit
python main_ui.py
The app will open in your browser (Gradio interface).

🧠 Tech Stack
Frontend/UI: Gradio

Audio Processing: SpeechRecognition, Pydub, Whisper

LLM: Groq with LLaMA-4-Scout

TTS: ElevenLabs

Backend: Python

Others: dotenv, os, logging

📌 Project Structure
bash
Copy
Edit
├── brain_of_the_llm.py       # Image analysis via LLM
├── voice_of_the_doctor.py    # Doctor's speech synthesis
├── voice_of_the_patient.py   # Voice recording & transcription
├── main_ui.py                # Main Gradio app
├── .env                      # API keys (not committed)
├── README.md
📣 Open to Suggestions & Collaboration
Have ideas to make this better? Want to contribute or use this for your own AI health project?

📬 Feel free to open an issue or connect with me on LinkedIn.

👨‍💻 Author
Sumit Yadav
🌐 Aspiring AI Developer | Open to Internships and Opportunities
📫 sumityad07

⚠️ This app is not a real medical tool. It is for demonstration and learning purposes only.

