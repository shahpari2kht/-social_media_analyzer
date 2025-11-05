import streamlit as st

st.set_page_config(page_title="Social Media Analyzer", layout="wide")
st.title("🪶 Social Media Analyzer (Public Demo)")
st.write("This is a mock Dashboard demonstrating Streamlit layout capability.")

col1, col2 = st.columns(2)
col1.markdown("### 📊 Topic Model (Mock)\nLDA Topics: اقتصاد، فرهنگ، سیاست، جامعه، فناوری")
col2.markdown("### 💬 Sentiment Trend (Mock)\nPositive: 42% | Neutral: 37% | Negative: 21%")

st.caption("Designed by Parisa Mohammadzadeh (shahpari2kht)")
