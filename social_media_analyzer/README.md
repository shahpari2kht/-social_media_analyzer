# 🧠 Social Media Analyzer  

Analyze Persian and multilingual social media text using NLP, topic modeling (LDA), and Streamlit dashboard visualization.

[![CI Tests](https://github.com/shahpari2kht/social_media_analyzer/actions/workflows/tests.yml/badge.svg)](https://github.com/shahpari2kht/social_media_analyzer/actions)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Repo Size](https://img.shields.io/github/repo-size/shahpari2kht/social_media_analyzer.svg)]()
[![Stars](https://img.shields.io/github/stars/shahpari2kht/social_media_analyzer.svg)]()

---

### 🔍 Features
- **LDA Topic Modeling** and Sentiment Analysis  
- Full **Persian Text Support** (`hazm`, `arabic-reshaper`, `python-bidi`, `wordcloud`)  
- Streamlit dashboard using **Vazir font** and Dark theme  
- Modular architecture with tests and CI integration  
- Public version for portfolio, Private version for production analysis  

### 🧱 Project Structure
social_media_analyzer/

│

├── src/

│ ├── preprocessing.py

│ ├── lda_model.py

│ ├── visualization.py

│ └── streamlit_app.py

├── tests/

├── docs/

│ └── architecture.png

├── requirements.txt

├── pyproject.toml

├── LICENSE

└── README.md

### 🚀 Running Locally
```bash
git clone git@github.com:shahpari2kht/social_media_analyzer.git
cd social_media_analyzer
pip install -r requirements.txt
streamlit run src/streamlit_app.py

🧪 CI/CD
The repository runs pytest automatically via GitHub Actions for every push on the main branch.
🌐 Author
Parisa Mohammadzadeh (shahpari2kht)

Data Scientist · NLP Enthusiast

📍 Ilam, Iran

✉️ shahpari2kht@gmail.com

🪩 GitHub/Profile

