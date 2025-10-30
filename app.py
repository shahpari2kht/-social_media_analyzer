import streamlit as st
from PIL import Image
import os

# === تنظیمات صفحه و تم عمومی === #
st.set_page_config(
    page_title="تحلیل موضوعات شبکه‌های اجتماعی",
    page_icon="🧠",
    layout="wide"
)

# === CSS تمام‌عیار برای نمایش فارسی + تم تیره === #
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css');

    html, body, .main, .block-container, [class*="css"] {
        background-color: #0d1117 !important;
        color: #f1f1f1 !important;
        font-family: 'Vazir', sans-serif !important;
    }
    h1, h2, h3, h4 {
        font-family: 'Vazir', sans-serif !important;
        color: #00b4d8 !important;
        text-align: center !important;
    }
    .topic-box {
        background-color: #1b263b;
        border-radius: 14px;
        padding: 25px;
        margin: 25px 0;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
        text-align: center;
    }
    .stSelectbox label {
        color: #ffffff !important;
        font-size: 16px;
        font-weight: bold;
    }
    hr {
        border: 1px solid #333;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# === مسیر داده‌ها === #
DATA_DIR = os.path.expanduser("~/social_media_analyzer/data")

# === کلمات کلیدی فرضی برای ۵ موضوع === #
TOPIC_KEYWORDS = {
    1: ["مدل", "داده", "یادگیری", "پژوهش", "نتیجه", "پایتون", "مقاله", "هوش‌مصنوعی"],
    2: ["داده‌کاوی", "تحلیل", "پست", "توییت", "کاربر", "جمع‌آوری", "متن", "شبکه"],
    3: ["ابزار", "پروژه", "کد", "منبع", "نمودار", "آزمایش", "پیش‌بینی", "پردازش"],
    4: ["احساس", "کار", "دیدگاه", "زمان", "تجربه", "کاربران", "نظرات", "تعامل"],
    5: ["پلتفرم", "سیستم", "وب", "آمار", "الگو", "فرآیند", "تحلیل‌گر", "ساختار"],
}

# === عنوان اصلی === #
st.markdown("<h1>🧠 داشبورد تحلیل موضوعات متنی</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#aaa;'>نمایش تعاملی LDA و WordCloud برای داده‌های شبکه‌های اجتماعی</p>", unsafe_allow_html=True)
st.markdown("<hr />", unsafe_allow_html=True)

# === انتخاب موضوع === #
selected_topic = st.selectbox("یکی از موضوعات زیر را انتخاب کنید:", range(1, 6))

# === نمایش اطلاعات هر موضوع === #
st.markdown(
    f"""
    <div class='topic-box' dir='rtl'>
        <h2 style='direction:rtl; unicode-bidi:bidi-override; display:inline-block;'>موضوع {selected_topic}</h2>
        <br>
        <p><b>کلمات کلیدی این موضوع:</b> {"، ".join(TOPIC_KEYWORDS[selected_topic])}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# === نمایش Wordcloud === #
image_path = os.path.join(DATA_DIR, f"wordcloud_topic_{selected_topic}.png")
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption=f"WordCloud برای موضوع {selected_topic}", use_container_width=True)
else:
    st.warning("فایل WordCloud مربوط به این موضوع در مسیر data یافت نشد.")


# === پاورقی === #
st.markdown("""
<hr />
<p style='text-align:center; color:gray; font-size:13px; direction:ltr;'>
Developed with ❤️ using Python & Streamlit
</p>
""", unsafe_allow_html=True)
