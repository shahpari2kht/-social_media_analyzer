# 🪶 Social Media Analyzer (Public Edition)

A simplified public version of the **Persian Social Media NLP Dashboard** designed by **Parisa Mohammadzadeh (shahpari2kht)**.  
This project demonstrates data science and NLP capabilities for **topic modeling, sentiment analysis**, and **dashboarding** with **Streamlit**.

---

<div align="right" dir="rtl">

## 🌍 هدف پروژه
ایجاد داشبوردی برای تحلیل محتوای شبکه‌های اجتماعی فارسی  
(نمایش موضوعات داغ، احساسات کاربران و ترندها)  
در محیط Streamlit با رابط کاربری راست‌چین و فونت وزیر.

</div>

---

## 🧩 Key Components

| Module | Description |
|--------|-------------|
| Preprocessing | Normalization and tokenization for Persian text (Hazm) |
| Topic Modeling | Extract 5 major topics from social media posts using *LDA (gensim)* |
| Visualization | Render dynamic WordClouds and sentiment charts (Streamlit + Matplotlib) |
| Utilities | Helper functions for data loading and cleaning |

---

## 🧠 Technologies Used

- **Python 3.11**
- **Streamlit**, **Pandas**, **Gensim**, **Hazm**
- **WordCloud**, **Matplotlib**, **Arabic-Reshaper**, **Python-Bidi**
- Font: *Vazir.ttf* (for RTL Persian display)

---

## 📊 Example Architecture
![architecture diagram](docs/architecture.png)

**High-level data flow:**
`collect → preprocess → topic_model → visualize → dashboard`

---

## 🚀 Demo Snapshot
Here’s an example mock screenshot of Streamlit dashboard layout:
![mock dashboard](assets/dashboard_mock.png)

---

## 🧩 Installation (Mock)
```bash
git clone https://github.com/shahpari2kht/social_media_analyzer.git
cd social_media_analyzer
pip install -r requirements.txt
streamlit run app_mock.py
🧪 Tests (Demonstration Only)
This public repo contains illustrative mock tests.

def test_mock():
assert True, "Placeholder test to demonstrate CI workflow!"
🧠 Skills Demonstrated
Domain	Skills
NLP	LDA, tokenization, normalization
Visualization	Streamlit dashboard, WordCloud
Configuration	Python packaging, pyproject.toml
CI/CD	GitHub Actions (pytest integration)
Documentation	README, License, workflow structure
🪪 License
MIT © 2025 Parisa Mohammadzadeh

This public edition contains no proprietary data or models.
