import json
import pandas as pd
from pathlib import Path

data_path = Path("data/sample_posts.json")
output_path = Path("data/reddit_posts_clean.csv")

with open(data_path, "r", encoding="utf-8") as f:
    raw = json.load(f)

posts = []
for post in raw["data"]["children"]:
    d = post["data"]
    posts.append({
        "id": d.get("id"),
        "title": d.get("title"),
        "author": d.get("author"),
        "score": d.get("score"),
        "num_comments": d.get("num_comments"),
        "created_utc": d.get("created_utc"),
        "url": d.get("url"),
        "selftext": d.get("selftext", "").replace("\n", " ").strip()
    })

df = pd.DataFrame(posts)
df.to_csv(output_path, index=False, encoding="utf-8")
print(f"✅ {len(df)} Reddit posts saved to {output_path}")
print(df.head(3))
