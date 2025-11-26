import streamlit as st
from groq import Groq
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="AFG Versatile AI", layout="wide")
st.markdown("<h1 style='text-align:center;background:linear-gradient(to right,black,red,green);color:white;padding:20px;border-radius:15px;'>افغانستان برای جهان ✪ AFG Versatile AI</h1>", unsafe_allow_html=True)

چت, عکس, ویدیو, صدا = st.tabs(["چت‌بات", "تولید عکس", "تولید ویدیو", "تولید صدا"])

with چت:
    st.header("چت‌بات قوی Llama 3")
    کلید = st.text_input("کلید Groq", type="password")
    if کلید:
        try:
            client = Groq(api_key=کلید)
            سوال = st.chat_input("سوال خود را بنویس")
            if سوال:
                st.chat_message("user").write(سوال)
                with st.chat_message("assistant"):
                    with st.spinner("در حال فکر کردن..."):
                        جواب = client.chat.completions.create(model="llama3-70b-8192", messages=[{"role":"user","content":سوال}])
                        st.write(جواب.choices[0].message.content)
        except:
            st.error("کلید اشتباه یا اینترنت قطع — دوباره امتحان کن")

with عکس: st.header("تولید عکس"); st.info("به زودی 🔥")
with ویدیو: st.header("تولید ویدیو"); st.info("به زودی 🔥")

with صدا:
    st.header("تولید صدا")
    متن = st.text_area("متن خود را بنویس")
    if st.button("صدا بساز") and متن:
        صدا = gTTS(متن, lang='fa')
        بافر = BytesIO()
        صدا.write_to_fp(بافر)
        بافر.seek(0)
        st.audio(بافر, format="audio/mp3")
        st.download_button("دانلود صدا", بافر, "afg_voice.mp3")
