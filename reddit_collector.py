import praw
import psycopg2
from datetime import datetime
from tqdm import tqdm

# ===========================
# Reddit API Config  👇
# ===========================
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="Linux:SocialMediaAnalyzer:v1.0 (by u/YOUR_USERNAME)"
)

# ===========================
# Database Config  👇
# ===========================
conn = psycopg2.connect(
    dbname="social_media_intel",
    user="postgres",
    password="",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# ===========================
# Collect Top Posts from Subreddits
# ===========================
subreddits = ["de", "european"]
for sub in subreddits:
    print(f"\n📥 Collecting from r/{sub}...")
    for post in tqdm(reddit.subreddit(sub).hot(limit=10)):
        cursor.execute("""
            INSERT INTO reddit_posts (title, author, subreddit, score, num_comments, created_utc, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            post.title,
            str(post.author),
            sub,
            post.score,
            post.num_comments,
            datetime.utcfromtimestamp(post.created_utc),
            post.url
        ))
        conn.commit()

conn.close()
print("\n✅ Data collection complete!")
