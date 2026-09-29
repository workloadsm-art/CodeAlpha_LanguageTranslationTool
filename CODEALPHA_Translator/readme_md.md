# Language Translation Tool 🌐

A user-friendly web application built with Python and Streamlit that translates text between multiple languages in real time. It also features integrated Text-to-Speech (TTS) functionality to listen to the translated output.

---

## 🌟 Features
* **Multi-language Translation:** Supports translation between English, Hindi, Urdu, Spanish, French, German, and Chinese.
* **Text-to-Speech (Audio Output):** Generates and plays audio for the translated text using Google Text-to-Speech (`gTTS`).
* **Clean UI:** Simple and clean web interface built using Streamlit.
* **Reliable API:** Powered by `deep-translator` (MyMemory API) for fast and reliable execution.

---

## 🛠️ Tech Stack & Dependencies
* **Programming Language:** Python 3.x
* **Frontend/UI:** Streamlit
* **Translation Library:** `deep-translator`
* **Audio Generation:** `gTTS` (Google Text-to-Speech)

---

## 🚀 How to Run Locally

### 1. Clone or Download the Project
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### 2. Install Dependencies
Run the following command in your terminal/command prompt:
```bash
pip install streamlit deep-translator gTTS
```

### 3. Run the Application
Execute the Streamlit app using:
```bash
python -m streamlit run app.py
```

---

## 📁 Repository Structure
```text
├── app.py                   # Main Streamlit application file
├── README.md                # Project documentation
└── translated_audio.mp3    # Temporary audio file (Generated at runtime)
```

---

## 👨‍💻 Developer Information
* **Task:** Task 1 - Language Translation Tool
* **Domain:** Artificial Intelligence / Python
* **Internship Program:** CodeAlpha AI Internship