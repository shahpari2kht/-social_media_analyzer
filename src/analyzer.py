import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# بارگذاری داده‌های تمیز
df = pd.read_csv("data/reddit_all_clean.csv").dropna(subset=["selftext"])

# فقط متن‌های کوتاه‌تر از 512 کاراکتر برای تست سریع
texts = df["selftext"].astype(str).apply(lambda t: t[:512]).tolist()

# مدل احساسات 🤖 (انگلیسی)
print("⚙️ Loading sentiment-analysis pipeline...")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiments = []
for t in tqdm(texts[:200]):  # فعلاً تا ۲۰۰ مورد برای تست
    try:
        result = sentiment_analyzer(t)[0]
        sentiments.append(result["label"])
    except Exception:
        sentiments.append("ERROR")

df["sentiment"] = sentiments + [""] * (len(df) - len(sentiments))

# ذخیره خروجی اولیه
df.to_csv("data/reddit_sentiment_sample.csv", index=False, encoding="utf-8")
print("✅ Sentiment analysis sample saved to data/reddit_sentiment_sample.csv")
