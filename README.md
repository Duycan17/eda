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
# eda
