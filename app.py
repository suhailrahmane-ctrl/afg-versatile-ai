```python
import streamlit as st
from groq import Groq
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="AFG Versatile AI", layout="wide")

st.markdown("""
<style>
    .big-title {font-size: 50px; text-align: center; background: linear-gradient(to right, black, red, green); 
                color: white; padding: 25px; border-radius: 15px; font-weight: bold; margin-bottom: 30px;}
</style>
<h1 class="big-title">افغانستان برای جهان ✪ AFG Versatile AI</h1>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["چت‌بات", "تولید عکس", "تولید ویدیو", "تولید صدا"])

with tab1:
    st.header("چت‌بات فوق قوی Llama 3")
    api_key = st.text_input("Groq API Key خود را اینجا بچسبان", type="password", help="از console.groq.com رایگان بگیر")
    if api_key:
        try:
            client = Groq(api_key=api_key)
            prompt = st.chat_input("اینجا سوال خود را بنویس...")
            if prompt:
                with st.chat_message("user"):
                    st.write(prompt)
                with st.chat_message("assistant"):
                    with st.spinner("در حال فکر کردن..."):
                        resp = client.chat.completions.create(
                            messages=[{"role": "user", "content": prompt}],
                            model="llama3-70b-8192",
                            temperature=0.7
                        )
                        answer = resp.choices[0].message.content
                        st.write(answer)
        except:
            st.error("کلید اشتباه است یا اینترنت قطع است")

with tab2:
    st.header("تولید عکس")
    st.info("به زودی با Stable Diffusion واقعی میاد 🔥")

with tab3:
    st.header("تولید ویدیو")
    st.info("به زودی با مدل جدید میاد 🔥")

with tab4:
    st.header("تولید صدا (کاملاً کار می‌کنه)")
    text = st.text_area("متن دلخواه خود را بنویس")
    if st.button("صدا بساز") and text:
        tts = gTTS(text, lang='fa')
        audio = BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        st.audio(audio, format="audio/mp3")
        st.download_button("دانلود صدا", audio, "afg_voice.mp3")
