import os
from deep_translator import MyMemoryTranslator
from gtts import gTTS
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Language Translation Tool", layout="centered")
st.title("🌐 Language Translation Tool")

# Language Mapping Dictionary
languages = {
    "English": "english",
    "Hindi": "hindi",
    "Urdu": "urdu",
    "Spanish": "spanish",
    "French": "french",
    "German": "german",
    "Chinese": "chinese",
}

# Input Text Area
input_text = st.text_area("Enter text to translate:", height=150)

# Language Selectors
col1, col2 = st.columns(2)
with col1:
  source_lang = st.selectbox(
      "Source Language:", list(languages.keys()), index=0
  )
with col2:
  target_lang = st.selectbox(
      "Target Language:", list(languages.keys()), index=2
  )

# Translate Button Action
if st.button("Translate"):
  if input_text.strip():
    try:
      src_code = languages[source_lang]
      tgt_code = languages[target_lang]

      # Translate Text
      translated_text = MyMemoryTranslator(
          source=src_code, target=tgt_code
      ).translate(input_text)

      # Display Result
      st.success("Translated Output:")
      st.text_area("Result:", value=translated_text, height=150)

      # Optional Text-to-Speech Feature
      gtts_lang_codes = {
          "English": "en",
          "Hindi": "hi",
          "Urdu": "ur",
          "Spanish": "es",
          "French": "fr",
          "German": "de",
          "Chinese": "zh-CN",
      }

      audio_lang = gtts_lang_codes.get(target_lang, "en")
      tts = gTTS(text=translated_text, lang=audio_lang)
      tts.save("translated_audio.mp3")
      st.audio("translated_audio.mp3", format="audio/mp3")

    except Exception as e:
      st.error(f"Error: {e}")
  else:
    st.warning("Please enter some text!")