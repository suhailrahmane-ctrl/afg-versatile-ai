import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="AFG Versatile AI", layout="wide")
st.markdown("<h1 style='text-align:center;background:linear-gradient(to right,black,red,green);color:white;padding:25px;border-radius:15px;font-weight:bold;'>افغانستان برای جهان ✪ AFG Versatile AI</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["چت‌بات", "تولید عکس", "تولید ویدیو", "تولید صدا"])

with tab1:
    st.header("چت‌بات هوشمند")
    msg = st.chat_input("اینجا بنویس...")
    if msg:
        st.chat_message("user").write(msg)
        st.chat_message("assistant").write(f"سلام داداش! تو گفتی: '{msg}' — افغانستان برای جهان! چی دیگه می‌خوای بدونی؟ 🇦🇫")

with tab2:
    st.header("تولید عکس")
    st.info("به زودی با FLUX.1 واقعی 🔥")

with tab3:
    st.header("تولید ویدیو")
    st.info("به زودی با مدل جدید 🔥")

with tab4:
    st.header("تولید صدا (کاملاً کار می‌کنه)")
    text = st.text_area("متن خود را بنویس")
    if st.button("صدا بساز") and text:
        with st.spinner("در حال ساخت صدا..."):
            tts = gTTS(text, lang='fa')
            audio = BytesIO()
            tts.write_to_fp(audio)
            audio.seek(0)
            st.audio(audio, format="audio/mp3")
            st.download_button("دانلود صدا", audio, "afg_voice.mp3")
        st.success("صدات آماده شد برادر! 🇦🇫")
