![Build Status](https://github.com/shahpari2kht/DataScoutBot/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen)

# 🤖 DataScoutBot
---

## ⚙️ اجزای اصلی

| ماژول | توضیح |
|-------|--------|
| **Bot** (Aiogram) | دریافت فرمان‌های کاربر مانند `/scrape` و مدیریت پیام‌ها |
| **Scraper** (Aiohttp + BeautifulSoup) | استخراج داده‌های نمونه از `books.toscrape.com` |
| **Dashboard** (Streamlit) | نمایش آنی داده‌ها و نمودارها با قابلیت **Auto‑Refresh** |

---

## 📁 ساختار پوشه‌ها
app/

├── bot/ ← منطق ربات تلگرام و فرمان‌ها

├── scraper/ ← فانکشن‌های جمع‌آوری داده و ذخیره در CSV

└── web_demo/ ← اجرای داشبورد Streamlit و رفرش خودکار


---

## 🚀 اجرای محلی

**ترمینال ۱:**
```bash
python app/bot/main.py

ترمینال ۲:

streamlit run app/web_demo/app.py

🧠 نکات و یادگیری‌ها
کار با async I/O در پایتون (aiohttp)
اتصال همزمان Bot و داشبورد وب
اجرای Thread‑based Auto‑Refresh در Streamlit
مانیتور تغییرات فایل (Event Monitoring)
👩‍💻 توسعه‌دهنده
طراحی و توسعه: Parisa Mohammadzadeh (shahpari2kht)

📍Iran

✉️ shahpari2kht@gmail.com

🔒 این نسخه برای بررسی عمومی منتشر شده.

فایل‌های حساس (توکن‌ها، داده‌های خروجی واقعی) در نسخه‌ی خصوصی نگهداری می‌شوند.


