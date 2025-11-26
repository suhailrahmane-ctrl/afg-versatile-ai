import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="AFG Versatile AI", layout="wide")
st.markdown("<h1 style='text-align: center; background: linear-gradient(to right, black, red, green); color: white; padding: 20px; border-radius: 15px;'>افغانستان برای جهان ✪ AFG Versatile AI</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["چت‌بات", "تولید عکس", "تولید ویدیو", "تولید صدا"])

with tab1:
    st.header("چت‌بات ساده (بدون کلید)")
    prompt = st.chat_input("سوال خود را بنویس (دری/پشتو/انگلیسی)")
    if prompt:
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            st.write("سلام داداش! تو گفتی: '" + prompt + "' — من Grok هستم و می‌گم افغانستان برای جهان! چی دیگه می‌خوای بدونی؟ 🇦🇫")

with tab2:
    st.header("تولید عکس")
    prompt_img = st.text_input("چی بسازم؟ (مثل: کوه‌های هندوکش)")
    if st.button("عکس بساز") and prompt_img:
        st.info("عکس '" + prompt_img + "' تصور شد! (به زودی واقعی با DALL-E) 🔥")

with tab3:
    st.header("تولید ویدیو")
    st.info("به زودی با مدل Sora 🔥")

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
