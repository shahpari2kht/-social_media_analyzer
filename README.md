# 📊 Social Media Analyzer / تحلیل شبکه‌های اجتماعی

**Python-based tool for collecting, analyzing, and visualizing social media data from public sources.**  
ابزاری برای جمع‌آوری، تحلیل و بصری‌سازی داده‌های شبکه‌های اجتماعی از منابع عمومی.

---

## 🧩 Modules / ماژول‌ها

| Module / ماژول | Description / توضیح |
|----------------|-------------------|
| `scraper/`     | Asynchronous data collector (API & HTML) / جمع‌آوری داده‌ها به صورت همزمان با استفاده از API و HTML |
| `app/`         | Main application pipeline / مسیر اصلی اجرای برنامه |
| `web_demo/`    | Interactive dashboard / داشبورد تعاملی |
| `docs/`        | Documentation & architecture diagrams / مستندات و نمودارهای معماری |

---

## 📁 Project Structure / ساختار پروژه


social_media_analyzer/
├── app/
│ ├── main.py
│ ├── scraper/
│ │ └── scraper.py
│ ├── web_demo/
│ │ ├── app.py
│ │ └── bridge.py
├── docs/
│ └── architecture.png
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── social_media_analyzer_private/ # Private tokens & datasets / داده‌ها و توکن‌های خصوصی



---

## 🚀 Installation & Running Locally / نصب و اجرای محلی

**Step 1 / مرحله ۱: Create virtual environment / ایجاد محیط مجازی**
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
Step 2 / مرحله ۲: Install dependencies / نصب پیش‌نیازها


pip install -r requirements.txt
Step 3 / مرحله ۳: Run the application / اجرای برنامه


python app/main.py
Or launch the interactive dashboard / یا اجرای داشبورد تعاملی:


streamlit run app/web_demo/app.py
🧠 Key Learnings / نکات کلیدی
End-to-end social media analytics pipeline / مسیر کامل تحلیل داده شبکه‌های اجتماعی

Integration of asyncio + aiohttp for concurrent scraping / استفاده از asyncio و aiohttp برای جمع‌آوری همزمان داده‌ها

Data cleaning and NLP analysis with spaCy and TextBlob / پاک‌سازی داده و تحلیل متون با spaCy و TextBlob

Interactive dashboards and live reporting with Streamlit / داشبورد تعاملی و گزارش‌گیری زنده با Streamlit

👩‍💻 Author / نویسنده
Parisa Mohammadzadeh – Data Scientist & Developer / دانشمند داده و توسعه‌دهنده
📍 Iran / ایران
📧 shahpari2kht@gmail.com
🔗 GitHub Profile

🔒 Notes / نکات امنیتی
Contains only public components / شامل تنها بخش‌های عمومی است

Private tokens, dataset samples, and deployment configurations are stored separately / توکن‌ها، نمونه داده‌ها و تنظیمات خصوصی جدا نگه داشته شده‌اند

Ensure sensitive data is never committed to this repository / مطمئن شوید داده‌های حساس هرگز به مخزن عمومی اضافه نشوند
