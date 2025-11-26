import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="AFG Versatile AI", layout="wide")
st.markdown("<h1 style='text-align:center;background:linear-gradient(to right,black,red,green);color:white;padding:25px;border-radius:15px;font-weight:bold;'>AFG Versatile AI</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["چت‌بات", "تولید عکس", "تولید ویدیو", "تولید صدا", "کد نویسی"])

# Chatbot
with tab1:
    st.header("چت‌بات هوشمند")
    msg = st.chat_input("اینجا بنویس...")
    if msg:
        st.chat_message("user").write(msg)
        st.chat_message("assistant").write(f"سلام! تو گفتی: '{msg}' — افغانستان برای جهان! چی دیگه می‌خوای بدونی؟")

# Generate Image
with tab2:
    st.header("تولید عکس")
    st.info("به زودی با FLUX.1 🔥")

# Generate Video
with tab3:
    st.header("تولید ویدیو")
    st.info("به زودی با Wan 2.2 🔥")

# Generate Voice
with tab4:
    st.header("تولید صدا")
    text = st.text_area("متن خود را بنویس")
    if st.button("صدا بساز") and text:
        with st.spinner("در حال ساخت..."):
            tts = gTTS(text, lang='fa')
            audio = BytesIO()
            tts.write_to_fp(audio)
            audio.seek(0)
            st.audio(audio, format="audio/mp3")
            st.download_button("دانلود", audio, "afg_voice.mp3")
        st.success("صدات آماده شد!")

# Code Generation
with tab5:
    st.header("کد نویسی با نمونه ساده")
    prompt_code = st.text_area("چی می‌خوای کدش ساخته شود؟")
    if st.button("کد بساز") and prompt_code:
        st.info("کد تولید شد! (به زودی با Code Llama)")
        st.code("def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)")
