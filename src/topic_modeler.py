import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- مرحله ۱: خواندن داده ---
data_path = "data/reddit_all_clean.csv"
df = pd.read_csv(data_path)

# اگر ستون 'title' و 'selftext' وجود دارد، ادغام‌مان را انجام بده
if 'selftext' in df.columns:
    df['text'] = df['title'].fillna('') + ' ' + df['selftext'].fillna('')
else:
    df['text'] = df['title'].fillna('')

# --- مرحله ۲: پاکسازی اولیه ---
texts = df['text'].fillna('').tolist()

# --- مرحله ۳: تبدیل متن به ماتریس کلمه ---
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
X = vectorizer.fit_transform(texts)

# --- مرحله ۴: مدل LDA برای کشف موضوعات ---
lda_model = LatentDirichletAllocation(n_components=5, random_state=42)
lda_model.fit(X)

# --- مرحله ۵: استخراج واژه‌ها برای هر موضوع ---
words = vectorizer.get_feature_names_out()
topics = []
for topic_idx, topic in enumerate(lda_model.components_):
    top_words = [words[i] for i in topic.argsort()[:-11:-1]]
    topics.append(top_words)
    print(f"موضوع {topic_idx + 1}: {', '.join(top_words)}")

# --- مرحله ۶: تولید WordCloud ---
for i, topic_words in enumerate(topics):
    wc = WordCloud(width=800, height=400, background_color='white').generate(' '.join(topic_words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"WordCloud موضوع {i + 1}")
    plt.savefig(f"data/wordcloud_topic_{i + 1}.png")
    plt.close()

print("\n✅ تحلیل موضوعی کامل شد: ۵ WordCloud در مسیر data ذخیره شدند.")
