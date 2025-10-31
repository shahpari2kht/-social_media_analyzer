# 🧠 Social Media Analyzer

A **Streamlit dashboard** for performing topic modeling on social media text data using **Latent Dirichlet Allocation (LDA)** and visualizing results with **WordClouds**.

---

## 🚀 Overview
This project processes text-based social media content in Persian and other languages, extracts **hidden topics** via LDA, and generates WordCloud images for each topic.  
It features an interactive dashboard with **Dark Mode**, full **Persian script compatibility**, and clean visualization for data exploration.

---

## ✨ Features
- **5 topics** extracted using LDA  
- Automatic WordCloud generation (`wordcloud_topic_1.png` ... `wordcloud_topic_5.png`)  
- Dark Mode UI for comfortable viewing  
- RTL text rendering with the Persian **Vazir** font  
- Simple local deployment with Streamlit  

---

## 📊 Dashboard Preview

| **Overview** | **Example Topic (3)** |
|--------------|-----------------------|
| ![Dashboard Overview](data/dashboard_overview.png) | ![Topic 3 WordCloud](data/topic3_wordcloud.png) |

---

## ⚙️ Installation & Usage
```bash
# Clone the repository
git clone https://github.com/shahpari2kht/social_media_analyzer.git
cd social_media_analyzer

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit dashboard
streamlit run app.py
Once running, the dashboard will open in your web browser.

All WordCloud images and topic data are stored inside the data/ directory.


🧩 Project Structure
social_media_analyzer/
├── app.py
├── src/
│   └── topic_modeler.py
├── data/
│   ├── wordcloud_topic_1.png
│   ├── wordcloud_topic_2.png
│   ├── wordcloud_topic_3.png
│   ├── wordcloud_topic_4.png
│   ├── wordcloud_topic_5.png
│   ├── dashboard_overview.png
│   └── topic3_wordcloud.png
├── requirements.txt
└── README.md

📚 Technologies Used
.Python 3.10+
.Streamlit
.NLTK & Gensim
.Matplotlib & WordCloud
.RTL-friendly CSS styling for Persian

👩‍💻 Author
Parisa Mohammadzadeh

📍 Ilam, Iran

🌐 GitHub: shahpari2kht

🇮🇷 توضیح کوتاه به فارسی
این پروژه یک داشبورد تحت Streamlit برای تحلیل داده‌های متنی شبکه‌های اجتماعی است.

با استفاده از مدل LDA، پنج موضوع اصلی استخراج و برای هر موضوع یک WordCloud تولید می‌شود.

ویژگی مهم آن پشتیبانی کامل از زبان فارسی (فونت وزیر، راست‌چین) و نمایش نتایج به صورت گرافیکی است، که برای پژوهش، مارکتینگ، یا تحلیل ترندها بسیار کاربردی است
