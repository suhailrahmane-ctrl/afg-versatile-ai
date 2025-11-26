import streamlit as st
from groq import Groq
from gtts import gTTS
from io import BytesIO
import time

st.set_page_config(page_title="AFG Versatile AI", layout="wide")

st.markdown("""
<style>
    .big-title {font-size: 50px; text-align: center; background: linear-gradient(to right, black, red, green);
                color: white; padding: 25px; border-radius: 15px; font-weight: bold;}
</style>
<h1 class="big-title">افغانستان برای جهان ✪ AFG Versatile AI</h1>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["چت‌بات", "تولید عکس", "تولید ویدیو", "تولید صدا"])

with tab1:
    st.header("چت‌بات قوی Llama 3")
    api_key = st.text_input("Groq API Key", type="password", value=st.session_state.get("groq_key", ""))
    
    if api_key:
        st.session_state.groq_key = api_key
        try:
            client = Groq(api_key=api_key.strip())
            prompt = st.chat_input("سوال خود را بنویس")
            if prompt:
                with st.chat_message("user"): st.write(prompt)
                with st.chat_message("assistant"):
                    with st.spinner("در حال فکر کردن..."):
                        resp = client.chat.completions.create(
                            messages=[{"role": "user", "content": prompt}],
                            model="llama3-70b-8192",
                            timeout=60
                        )
                        st.write(resp.choices[0].message.content)
        except Exception as e:
            st.error("کلید اشتباه یا اینترنت قطع است. دوباره امتحان کن.")

with tab2: st.header("تولید عکس"); st.info("به زودی 🔥")
with tab3: st.header("تولید ویدیو"); st.info("به زودی 🔥")

with tab4:
    st.header("تولید صدا")
    text = st.text_area("متن را بنویس")
    if st.button("صدا بساز") and text:
        tts = gTTS(text, lang='fa')
        audio = BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        st.audio(audio, format="audio/mp3")
        st.download_button("دانلود صدا", audio, "afg_voice.mp3")
