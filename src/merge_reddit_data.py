import json, pandas as pd
from pathlib import Path

raw_dir = Path("data/raw")
all_posts = []

for json_file in raw_dir.glob("*_posts.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            # فقط فایل‌هایی که ساختار درست Reddit API دارند
            if isinstance(data, dict) and "data" in data and "children" in data["data"]:
                for post in data["data"]["children"]:
                    p = post.get("data", {})
                    all_posts.append({
                        "subreddit": p.get("subreddit"),
                        "id": p.get("id"),
                        "title": p.get("title"),
                        "author": p.get("author"),
                        "score": p.get("score"),
                        "num_comments": p.get("num_comments"),
                        "created_utc": p.get("created_utc"),
                        "url": p.get("url"),
                        "selftext": (p.get("selftext") or "").replace("\n", " ").strip()
                    })
            else:
                print(f"⚠️ Skipping {json_file.name} (invalid or empty format)")
        except Exception as e:
            print(f"❌ Error parsing {json_file.name}: {e}")

df = pd.DataFrame(all_posts)
df.drop_duplicates(subset=["id"], inplace=True)
df.to_csv("data/reddit_all_clean.csv", index=False, encoding="utf-8")

print(f"✅ Saved {len(df)} combined posts to data/reddit_all_clean.csv")
