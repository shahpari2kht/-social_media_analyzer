# 📊 Social Media Analyzer

A Python based analytical tool designed to **collect, clean, and visualize social media data** from multiple public sources.  
It provides sentiment analysis, engagement metrics, and topic extraction for research and business insights.

---

## ⚙️ Core Components

| Module | Description |
|--------|-------------|
| `scraper/` | Asynchronous data collector (API & HTML) |
| `analyzer/` | NLP-based text processor and sentiment analyzer |
| `visualizer/` | Interactive visualization and dashboard tools |
| `tests/` | Unit tests for each functional module |

---

## 📁 Project Structure

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
└── README.md


---

## 🚀 Running Locally

**Step 1.** Create a virtual environment  
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

Step 2. Install dependencies
pip install -r requirements.txt

Step 3. Run the application
python app/main.py

or launch the interactive dashboard:

streamlit run app/web_demo/app.py



🧠 Key Learnings
End-to-end data pipeline for social media analytics

Integration of asyncio with aiohttp for concurrent scraping

Data cleaning and NLP analysis using spaCy and textblob

Live visualization and reporting with Streamlit

👩‍💻 Author
Parisa Mohammadzadeh
Data Scientist & Developer
📍 Iran
📧 shahpari2kht@gmail.com
🔗 GitHub Profile

🔒 Note
This repository contains only non-sensitive public components.
Private tokens, dataset samples, and deployment configurations are stored separately in the private version of this project.
