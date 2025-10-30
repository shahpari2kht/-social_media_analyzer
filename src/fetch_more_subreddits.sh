#!/bin/bash
# --- Collect datasets from multiple subreddits ---
mkdir -p data/raw
SUBS=("datascience" "MachineLearning" "ArtificialIntelligence" "datasets" "careerguidance")

for s in "${SUBS[@]}"; do
  echo "📥 Fetching from r/$s ..."
  curl -A "Mozilla/5.0 (Linux)" "https://api.reddit.com/r/$s/?limit=100" -o "data/raw/${s}_posts.json"
  sleep 2
done

echo "✅ Finished collecting data from ${#SUBS[@]} subreddits."
