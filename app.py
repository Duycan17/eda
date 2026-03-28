from __future__ import annotations

import re
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_FILES = [
    ("Tripadvisor", "bts_skytrain_reviews.csv"),
    ("Reddit", "bts_reddit_reviews_large.csv"),
]

STOP_WORDS = {
    "about",
    "after",
    "again",
    "airport",
    "also",
    "and",
    "are",
    "around",
    "bangkok",
    "been",
    "bts",
    "but",
    "can",
    "could",
    "for",
    "from",
    "get",
    "had",
    "has",
    "have",
    "hotel",
    "just",
    "line",
    "not",
    "our",
    "out",
    "people",
    "really",
    "should",
    "skytrain",
    "that",
    "the",
    "their",
    "there",
    "they",
    "this",
    "train",
    "very",
    "was",
    "were",
    "what",
    "when",
    "with",
    "you",
    "your",
}


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [col.replace("\ufeff", "").strip() for col in df.columns]
    return df


@st.cache_data(show_spinner=False)
def load_data(base_dir: Path) -> tuple[pd.DataFrame, dict[str, float]]:
    frames: list[pd.DataFrame] = []

    for source_name, file_name in DATA_FILES:
        path = base_dir / file_name
        df = pd.read_csv(path, encoding="utf-8-sig")
        df = _normalize_columns(df)
        df["source"] = source_name
        frames.append(df)

    data = pd.concat(frames, ignore_index=True)

    data["review_rating_num"] = pd.to_numeric(data["review_rating"], errors="coerce")
    data["like_count_num"] = pd.to_numeric(data["like_count"], errors="coerce")
    data["images_count_num"] = pd.to_numeric(data["images_count"], errors="coerce")

    published = pd.to_datetime(data["published_date"], errors="coerce", format="mixed")
    created = pd.to_datetime(data["created_at_date"], errors="coerce", format="mixed")
    data["review_date"] = published.fillna(created)
    data["review_date_only"] = data["review_date"].dt.date

    data["review_text"] = data["review_text"].fillna("")
    data["review_title"] = data["review_title"].fillna("")
    data["full_text"] = (data["review_title"] + " " + data["review_text"]).str.strip()

    reddit_mask = data["source"].eq("Reddit")
    reddit_scores = data.loc[reddit_mask, "review_rating_num"].dropna()
    reddit_q1 = float(reddit_scores.quantile(0.25)) if not reddit_scores.empty else 0.0
    reddit_q3 = float(reddit_scores.quantile(0.75)) if not reddit_scores.empty else 0.0

    def derive_sentiment(row: pd.Series) -> str:
        rating = row["review_rating_num"]
        if pd.isna(rating):
            return "Unknown"
        if row["source"] == "Tripadvisor":
            if rating >= 4:
                return "Positive"
            if rating <= 2:
                return "Negative"
            return "Neutral"
        if rating >= reddit_q3:
            return "Positive"
        if rating <= reddit_q1:
            return "Negative"
        return "Neutral"

    data["sentiment"] = data.apply(derive_sentiment, axis=1)
    return data, {"reddit_q1": reddit_q1, "reddit_q3": reddit_q3}


def top_words(text_series: pd.Series, n: int = 20) -> pd.DataFrame:
    text = " ".join(text_series.dropna().astype(str)).lower()
    tokens = re.findall(r"[a-z]{3,}", text)
    filtered = [token for token in tokens if token not in STOP_WORDS]
    if not filtered:
        return pd.DataFrame(columns=["word", "count"])
    counts = pd.Series(filtered).value_counts().head(n)
    return counts.rename_axis("word").reset_index(name="count")


def main() -> None:
    st.set_page_config(page_title="BTS Reviews EDA Dashboard", layout="wide")
    st.title("BTS Reviews EDA Dashboard")
    st.caption("Combined analysis of Tripadvisor and Reddit review data.")

    base_dir = Path(__file__).resolve().parent
    data, _ = load_data(base_dir)

    st.sidebar.header("Filters")
    sources = sorted(data["source"].dropna().unique().tolist())
    selected_sources = st.sidebar.multiselect(
        "Source",
        options=sources,
        default=sources,
    )

    lines = sorted(data["bts_line"].dropna().astype(str).unique().tolist())
    selected_lines = st.sidebar.multiselect("BTS line", options=lines, default=lines)

    languages = sorted(data["review_language"].dropna().astype(str).unique().tolist())
    selected_languages = st.sidebar.multiselect(
        "Language",
        options=languages,
        default=languages,
    )

    sentiments = ["Positive", "Neutral", "Negative", "Unknown"]
    selected_sentiments = st.sidebar.multiselect(
        "Sentiment",
        options=sentiments,
        default=sentiments,
    )

    min_date = data["review_date_only"].dropna().min()
    max_date = data["review_date_only"].dropna().max()

    if min_date is not None and max_date is not None:
        start_date, end_date = st.sidebar.date_input(
            "Date range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
        )
    else:
        start_date, end_date = None, None

    keyword = st.sidebar.text_input("Keyword contains", value="").strip().lower()

    filtered = data.copy()
    filtered = filtered[filtered["source"].isin(selected_sources)]
    filtered = filtered[filtered["bts_line"].astype(str).isin(selected_lines)]
    filtered = filtered[filtered["review_language"].astype(str).isin(selected_languages)]
    filtered = filtered[filtered["sentiment"].isin(selected_sentiments)]

    if start_date is not None and end_date is not None:
        date_mask = filtered["review_date_only"].between(start_date, end_date)
        filtered = filtered[date_mask]

    if keyword:
        keyword_mask = filtered["full_text"].str.lower().str.contains(keyword, na=False)
        filtered = filtered[keyword_mask]

    if filtered.empty:
        st.warning("No rows match the current filter set.")
        return

    total_reviews = len(filtered)
    avg_rating = filtered["review_rating_num"].mean()
    positive_share = (
        filtered["sentiment"].eq("Positive").mean() * 100 if total_reviews else 0.0
    )
    date_min = filtered["review_date"].min()
    date_max = filtered["review_date"].max()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Reviews", f"{total_reviews:,}")
    c2.metric("Average Rating/Score", f"{avg_rating:.2f}" if pd.notna(avg_rating) else "N/A")
    c3.metric("Positive Share", f"{positive_share:.1f}%")
    c4.metric(
        "Date Coverage",
        f"{date_min.date()} to {date_max.date()}" if pd.notna(date_min) and pd.notna(date_max) else "N/A",
    )

    left, right = st.columns(2)

    sentiment_by_source = (
        filtered.groupby(["source", "sentiment"], as_index=False)
        .size()
        .rename(columns={"size": "count"})
    )
    fig_sentiment = px.bar(
        sentiment_by_source,
        x="source",
        y="count",
        color="sentiment",
        barmode="stack",
        title="Sentiment Distribution by Source",
    )
    left.plotly_chart(fig_sentiment, use_container_width=True)

    rating_dist = filtered.dropna(subset=["review_rating_num"])
    fig_rating = px.histogram(
        rating_dist,
        x="review_rating_num",
        color="source",
        nbins=30,
        title="Rating/Score Distribution",
    )
    right.plotly_chart(fig_rating, use_container_width=True)

    timeline = (
        filtered.dropna(subset=["review_date"])
        .groupby(
            [pd.Grouper(key="review_date", freq="W"), "source"],
            as_index=False,
        )
        .size()
        .rename(columns={"size": "count"})
        .sort_values("review_date")
    )
    fig_timeline = px.line(
        timeline,
        x="review_date",
        y="count",
        color="source",
        markers=True,
        title="Weekly Review Volume",
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

    left2, right2 = st.columns(2)

    top_lines = (
        filtered["bts_line"]
        .fillna("Unknown")
        .astype(str)
        .value_counts()
        .head(12)
        .rename_axis("bts_line")
        .reset_index(name="count")
    )
    fig_lines = px.bar(top_lines, x="count", y="bts_line", orientation="h", title="Top BTS Lines")
    left2.plotly_chart(fig_lines, use_container_width=True)

    language_counts = (
        filtered["review_language"]
        .fillna("Unknown")
        .astype(str)
        .value_counts()
        .head(12)
        .rename_axis("review_language")
        .reset_index(name="count")
    )
    fig_lang = px.pie(language_counts, names="review_language", values="count", title="Language Mix")
    right2.plotly_chart(fig_lang, use_container_width=True)

    st.subheader("Top Words in Selected Reviews")
    words = top_words(filtered["full_text"], n=20)
    if words.empty:
        st.write("No extractable words for the current filters.")
    else:
        fig_words = px.bar(words.sort_values("count"), x="count", y="word", orientation="h")
        st.plotly_chart(fig_words, use_container_width=True)

    preview_cols = [
        "source",
        "bts_line",
        "review_rating_num",
        "sentiment",
        "review_date",
        "review_language",
        "review_title",
        "review_text",
    ]
    st.subheader("Filtered Data Preview")
    st.dataframe(filtered[preview_cols], use_container_width=True, height=360)


if __name__ == "__main__":
    main()
