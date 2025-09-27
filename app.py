import streamlit as st
import random

st.set_page_config(page_title="For My SpiderQueen 🕷👑", page_icon="❤️")

# Custom CSS biar background pink dan font manis
st.markdown(
    '''
    <style>
    body {
        background-color: #ffe6f2; /* pink pastel */
        color: #ff1493; /* hot pink font */
        font-family: "Comic Sans MS", cursive, sans-serif;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff85c1;
        color: #fff;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Judul
st.markdown("<h1 style='text-align:center; color:deeppink;'>💌 For My SpiderQueen, Charlina 🕷👑</h1>", unsafe_allow_html=True)

# List kata-kata semangat romantis
quotes = [
    "Hai Charlina ❤️, ingat ya… kamu lebih kuat dari yang kamu kira 🌟",
    "SpiderQueen-ku 🕷👑, dunia boleh ribet tapi kamu selalu keren di mataku ✨",
    "Aku selalu di sini buat kamu, bahkan kalau kamu lagi capek 🌷",
    "Keep shining, Charlina ✨. Semua badai pasti reda 🌈",
    "Jangan lupa tersenyum hari ini ya 😘",
    "Aku bangga sama kamu, SpiderQueen-ku 💕"
]

# Tombol random kata
if st.button("✨ Kasih Aku Kata Manis ✨"):
    st.success(random.choice(quotes))
