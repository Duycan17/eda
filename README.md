# BTS Reviews EDA Dashboard

## Run

```bash
uv run streamlit run app.py
```

The dashboard loads:
- `bts_skytrain_reviews.csv`
- `bts_reddit_reviews_large.csv`

It derives `sentiment` from `review_rating`:
- Tripadvisor: 1-2 negative, 3 neutral, 4-5 positive
- Reddit: score quantile rule (Q1/Q3 computed from current dataset)

NLP-oriented cleaning is applied before analysis:
- URL/link removal
- Emoji normalization (`emoji` token)
- Hashtag removal
- Deduplication by (`source`, `review_id`) then by (`source`, cleaned text)

The dashboard displays a word cloud from cleaned review text.
# eda
