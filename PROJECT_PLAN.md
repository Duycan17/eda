# Project Plan

## Project Title
**Enhancing BTS Skytrain Services through Aspect-Based Sentiment Analysis of Passenger Reviews**

## 1. Executive Direction

This project should not stop at classifying reviews as positive or negative. To aim for a top score, the project should answer the question that BTS executives actually care about:

**Which specific service aspects are hurting passenger experience, at which touchpoints, and what action should management take first?**

That is the core reason to position the project as **Aspect-Based Sentiment Analysis (ABSA)** with a business consulting narrative, not just a standard sentiment classification exercise.

## 2. Project Objective

Build an end-to-end sentiment analytics pipeline for BTS Skytrain passenger reviews that:

- collects and cleans at least **2,000 real reviews/comments**
- compares at least **2 sentiment modeling approaches**
- evaluates performance with a **mandatory confusion matrix**
- explains the **business impact of Precision vs Recall**
- calculates **Net Sentiment Score (NSS)** and **sentiment trends over time**
- identifies the main service aspects driving praise and complaints
- produces at least **3 actionable recommendations** for BTS management
- delivers a **Jupyter Notebook**, **slides**, and a **10-15 page report**

## 3. Why This Topic Can Score 10

Most student projects will likely do only overall sentiment classification. This project becomes stronger and more distinctive if it delivers three layers:

- **Overall sentiment**: Are passengers satisfied or dissatisfied?
- **Aspect-level sentiment**: Are complaints about punctuality, crowding, cleanliness, ticketing, staff, or station facilities?
- **Management prioritization**: Which problem should BTS fix first based on complaint volume, severity, and business risk?

This turns the project from a technical demo into a consulting-grade decision tool.

## 4. Strict Guideline Compliance Map

### Phase 1: Data Acquisition & Preprocessing

- Use automated scraping with **Playwright/Selenium/BeautifulSoup**
- Collect at least **2,000 rows**
- Prefer multiple touchpoints to reduce bias:
- `Google Maps` reviews of major BTS stations/interchanges
- `TripAdvisor` reviews discussing BTS Skytrain experience
- `YouTube` comments from BTS travel/service videos
- Keep fields such as `review_text`, `rating`, `date`, `source`, `station_or_touchpoint`, `language`
- Clean noisy text:
- lowercase/normalize text where appropriate
- remove URLs, duplicates, spam, excessive punctuation
- handle emojis, slang, abbreviations, repeated characters
- standardize Thai-English mixed writing if present
- handle missing values
- Perform EDA:
- review count by source
- review length distribution
- rating distribution
- top words before cleaning vs after cleaning
- timeline of review volume
- language mix and missing-value profile

### Phase 2: Modeling & Evaluation

- Compare at least **2 methods**:
- **Model 1 (Traditional ML)**: TF-IDF + Linear SVM or Logistic Regression
- **Model 2 (Transformer/Deep Learning)**: XLM-RoBERTa, DeBERTa, or a multilingual review-suitable transformer
- Use a **confusion matrix** for both models
- Report **Accuracy, Precision, Recall, F1-score**
- Add **error analysis** with real sentence examples
- Explain **business trade-offs**:
- False Negatives on safety, breakdown, overcrowding, and accessibility complaints are high-risk because management may miss urgent service problems
- False Positives waste resources, but usually damage is lower than missing serious operational issues
- Therefore, for severe complaint detection, **Recall is strategically more important than Precision**

### Phase 3: Business Insights & Visualization

- Calculate **Net Sentiment Score (NSS)**:
- `NSS = (% Positive Reviews - % Negative Reviews) x 100`
- Plot **sentiment trend over time**
- Use **Word Clouds** for positive and negative reviews
- Add **Topic Modeling or aspect extraction** to reveal reasons behind sentiment
- Build a professional dashboard in **Plotly / Power BI / Tableau**
- Deliver at least **3 strategic recommendations**

### Phase 4: Deliverables

- `1` Jupyter Notebook with clear structure, comments, and smooth execution
- `2` Presentation slides, maximum **15 slides**, focused on storytelling
- `3` Comprehensive report, **10-15 pages**, fully documenting process, methodology, evaluation, error analysis, and business insights

## 5. Recommended Project Design

## Business Problem Framing

BTS Skytrain is a service business. Passenger dissatisfaction does not come from one single cause. It comes from a combination of issues such as crowding, delays, station accessibility, ticketing friction, staff support, cleanliness, heat, and interchange convenience. A simple polarity label is not enough for management. They need a ranked view of service pain points.

The project should therefore tell this story:

**“Passenger dissatisfaction is concentrated in a small number of service aspects. If BTS improves those specific weak points, overall sentiment and perceived service quality can rise measurably.”**

## 6. Data Strategy

## Data Sources

Use a **multi-source review dataset** so the project looks realistic and richer than a single-source assignment.

- `Source 1`: Google Maps reviews from selected BTS stations
- `Source 2`: TripAdvisor reviews mentioning BTS Skytrain experience
- `Source 3`: YouTube comments from commuter/travel videos about BTS service experience

Target a dataset of **2,500-4,000 rows** so the minimum requirement is safely exceeded after cleaning.

## Suggested Station / Touchpoint Selection

Focus on stations and contexts that naturally generate passenger opinions:

- Siam
- Asok
- Mo Chit
- Sala Daeng
- Victory Monument
- Phaya Thai
- Chatuchak-adjacent access points

This creates a practical angle for comparing busy interchange stations versus standard stations.

## Suggested Fields

- `review_id`
- `source`
- `date`
- `rating` if available
- `review_text`
- `station_or_context`
- `language`
- `clean_text`
- `sentiment_label`
- `aspect_tags`

## Labeling Strategy

To make the project more rigorous than average:

- Use rating-based weak labels only for initial bootstrapping
- Create a **manually reviewed gold dataset** for evaluation
- Manually label about **800-1,200 reviews** for final sentiment validation
- For ABSA, annotate aspect tags on a smaller subset of aspect-rich reviews or sentences

This is a strong academic move because it shows you understand that star ratings are imperfect proxies for sentiment.

## 7. Preprocessing Plan

- Remove duplicate reviews and near-duplicates
- Detect and remove obvious spam or non-informative entries
- Normalize whitespace, punctuation, elongated text, and repeated characters
- Convert emojis to sentiment cues or remove them consistently
- Expand common abbreviations and internet slang where feasible
- Keep a separate column for raw text and cleaned text
- If Thai and English are mixed, either:
- keep a multilingual pipeline, or
- translate to one working language with careful documentation

Recommended choice:

- Keep the original text when possible
- Use a multilingual model for the advanced approach
- Document language handling carefully in the report

That choice looks more advanced and more faithful to real customer data.

## 8. EDA Plan

The EDA should be strong enough to stand on its own in the report and slides.

Create:

- review volume by source
- review volume over time
- average review length by sentiment and source
- rating distribution
- missing-value table
- vocabulary comparison before cleaning vs after cleaning
- most common bigrams/trigrams
- station/touchpoint review volume comparison

Add one business-oriented EDA chart that other groups may not have:

- **Complaint concentration chart**: percentage of negative reviews contributed by the top 3 aspects or top 3 stations

That gives management a prioritization lens immediately.

## 9. Modeling Strategy

## Mandatory Comparison

Compare two core methods:

Recommended prediction setup:

- use **3 sentiment classes**: positive, neutral, negative
- apply a **stratified train/validation/test split**
- keep the same evaluation split for both models for a fair comparison

### Model A: Traditional Baseline

- TF-IDF vectorization
- Linear SVM or Logistic Regression
- hyperparameter tuning with `GridSearchCV`

Why this is good:

- fast
- interpretable
- strong benchmark
- satisfies the traditional ML comparison requirement

### Model B: Advanced Model

- Fine-tuned multilingual transformer such as XLM-RoBERTa or DeBERTa
- tuning with validation loss, learning-rate search, batch-size comparison, and early stopping

Why this is good:

- handles context better
- stronger performance on nuanced complaints, sarcasm, and mixed expressions
- makes the project visibly more advanced

## Tuning and Validation Plan

- use `GridSearchCV` for the traditional model
- test n-gram range, minimum document frequency, and regularization strength
- fine-tune the transformer with at least 2 learning-rate settings and 2 epoch settings
- compare macro F1 and class-wise Recall, not just overall Accuracy
- document the final model-selection rationale clearly in the report

## ABSA Layer

This is the “wow” component and should be presented as the strategic differentiator.

Define an aspect taxonomy such as:

- punctuality and waiting time
- crowding and comfort
- cleanliness
- staff attitude and helpfulness
- ticketing and payment
- accessibility and escalators/lifts
- safety and security
- station navigation and connectivity
- value for money

Recommended approach:

- extract candidate keywords/topics using `KeyBERT`, `BERTopic`, or frequency analysis
- refine them into a clean business taxonomy manually
- assign aspect tags to reviews or sentences
- compute aspect-level sentiment and aspect-level NSS

This makes the output far more executive-friendly than raw sentiment.

## 10. Evaluation Plan

The evaluation section should be one of the strongest parts of the project.

Report:

- confusion matrix for both main models
- precision
- recall
- F1-score
- macro average if classes are imbalanced

## Required Business Interpretation

Explain Precision vs Recall in BTS context:

- Missing a real complaint about safety, train delays, or severe crowding is costly because it hides real operational pain points
- Therefore, high **Recall** matters when the objective is service risk detection
- High **Precision** matters when recommending targeted investment, because false alarms can waste budget
- The final model choice should not be based only on highest accuracy, but on the metric that best matches BTS management needs

## Error Analysis

Include specific examples of model failure such as:

- mixed sentiment in one review
- sarcasm
- short slang-heavy comments
- reviews praising BTS overall but criticizing one station
- aspect conflict in the same sentence

This directly aligns with the guideline requirement for deep evaluation and makes the report look mature.

## 11. Business Insights Plan

## Core Metrics

- overall sentiment distribution
- NSS overall
- NSS by source
- NSS by aspect
- NSS over time
- negative aspect share

## Recommended Dashboard

Build a dashboard with:

- sentiment trend over time
- aspect-level sentiment breakdown
- station/touchpoint comparison
- positive word cloud
- negative word cloud
- top complaint drivers

## 12. Three High-Value Strategic Recommendations

Your final recommendations should be concrete, measurable, and linked to data.

Recommended direction:

### Recommendation 1

Prioritize **crowding and waiting-time mitigation** at high-traffic interchange stations during peak hours.

Possible actions:

- deploy platform flow control
- increase peak-hour train frequency if operationally feasible
- improve passenger load communication on screens and apps

### Recommendation 2

Fix recurring **accessibility and station-facility pain points**.

Possible actions:

- escalator and lift maintenance prioritization
- clearer signage for exits and transfers
- targeted improvement at stations with worst facility-related NSS

### Recommendation 3

Strengthen the **digital passenger feedback loop**.

Possible actions:

- monitor aspect-level sentiment weekly
- create an internal service-alert dashboard
- connect complaint trends to operations and customer service teams

## 13. The “Wow” Factor

To stand out from other groups, include one executive-grade feature:

## Option Chosen: BTS Service Pain Index

Create a custom composite index:

`Service Pain Index = Complaint Volume x Negative Sentiment Severity x Business Criticality`

Use it to rank aspects or stations. For example:

- crowding may have high complaint volume
- accessibility may have lower volume but higher criticality
- safety-related complaints may deserve top management attention even if counts are smaller

This is the strongest differentiator because it converts text analytics into an action-priority score.

## Optional Extra “Wow” Layer

If the team has enough time, add:

- a heatmap of aspect sentiment by station/touchpoint
- a before/after simulation such as:
- “If negative sentiment on crowding drops by 20%, projected NSS improves from X to Y”

That feels like consulting output, not just coursework.

## 14. Team Role Allocation

Follow the course role structure directly.

### Data Engineer

- scrape data from multiple sources
- clean and normalize text
- maintain data dictionary
- prepare EDA-ready dataset

### AI Developer / Data Scientist

- build baseline ML model
- fine-tune transformer model
- compare metrics and confusion matrices
- conduct error analysis

### Business Analyst

- calculate NSS
- build aspect-level dashboard
- produce visualizations and recommendations
- design the Service Pain Index

### Project Manager / Team Leader

- manage timeline and integration
- ensure notebook runs smoothly
- write the report
- design storytelling slides
- coordinate presentation rehearsal

## 15. Timeline Aligned with Guideline

### Week 5: Proposal Finalization

- confirm topic
- confirm data sources
- define aspect taxonomy draft
- assign team roles

### Week 6-7: Data Collection, Cleaning, and EDA

- scrape at least 2,500 rows
- clean and normalize text
- conduct full EDA
- finalize labeled subset for modeling

### Week 8-9: Modeling and Evaluation

- train baseline model
- train transformer model
- generate confusion matrices and metric comparison
- perform error analysis
- complete aspect-level sentiment outputs

### Week 10: Insights, Dashboard, Report, and Slides

- calculate NSS and trends
- build dashboard
- derive recommendations
- finalize notebook
- write 10-15 page report
- finalize 15-slide presentation

### Week 11: Defense Preparation

- rehearse presentation
- prepare short answers for likely Q&A
- verify notebook, visuals, and appendix evidence

## 16. Notebook Structure

The notebook should be clean and presentation-ready.

- `1` Business problem and objective
- `2` Data source and scraping process
- `3` Raw data preview
- `4` Cleaning and preprocessing
- `5` EDA
- `6` Labeling strategy
- `7` Model A
- `8` Model B
- `9` Evaluation and confusion matrix
- `10` Error analysis
- `11` ABSA / aspect extraction
- `12` NSS and trend analysis
- `13` Dashboard-ready outputs
- `14` Recommendations
- `15` Conclusion and limitations

## 17. Slide Plan

Keep slides under 15 and heavily story-driven.

- `1` Title and team roles
- `2` Business problem: why BTS should care
- `3` Project objective and business questions
- `4` Data sources and scale
- `5` Data cleaning challenges
- `6` EDA highlights
- `7` Modeling approach comparison
- `8` Model evaluation with confusion matrix
- `9` Precision vs Recall business trade-off
- `10` Aspect-based findings
- `11` NSS and sentiment trend
- `12` Dashboard / Service Pain Index
- `13` Top 3 recommendations
- `14` Expected business impact
- `15` Closing and Q&A

## 18. Report Plan

Write the report exactly in the direction required by the guideline.

- Introduction
- business context of BTS Skytrain
- project objectives
- why passenger review analytics matters

- Data Strategy
- data sources
- scraping process
- dataset description
- preprocessing challenges
- EDA findings

- Methodology
- sentiment labeling strategy
- feature engineering
- model choice justification
- hyperparameter tuning
- ABSA design

- Model Evaluation
- confusion matrices
- precision, recall, F1
- business trade-off interpretation
- error analysis with examples

- Business Insights
- NSS
- trend charts
- aspect-level findings
- Service Pain Index
- recommendations

- Conclusion
- summary
- business value
- limitations
- future improvement

## 19. Key Risks and How to Handle Them

- `Risk`: not enough usable reviews after cleaning
- `Action`: collect 2,500-4,000 rows initially

- `Risk`: multilingual and mixed-language complexity
- `Action`: use multilingual transformer and document language policy clearly

- `Risk`: weak labels from ratings are noisy
- `Action`: build a manually validated gold subset

- `Risk`: ABSA becomes too broad
- `Action`: limit to 6-9 high-value aspects only

- `Risk`: dashboard becomes decorative instead of analytical
- `Action`: connect every chart to a management decision

## 20. Final Positioning Statement

If executed well, this project can stand out because it is not just:

- “Are reviews positive or negative?”

It becomes:

- “Which exact BTS service problems create dissatisfaction, how severe are they, where do they appear, and what should management fix first?”

That is the level of framing most likely to impress the lecturer, satisfy the guideline strictly, and create a clear “wow” effect.
