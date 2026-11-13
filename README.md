# India App Experience Index

### Turning millions of consumer opinions into actionable product intelligence.

**India App Experience Index** is an independent product analytics project designed to evaluate and benchmark the user experience of popular consumer applications in India using publicly available Google Play reviews.

The project combines review mining, AI-powered feedback classification, sentiment analysis, product experience scoring and hands-on product audits to identify recurring user frustrations and actionable product improvement opportunities.

---

## 1. Problem Statement

India has a rapidly growing digital consumer ecosystem, with millions of users interacting with fintech, commerce, food delivery, mobility and content applications every day.

However, understanding the actual user experience across these applications is challenging.

App ratings alone do not explain:
- Why users are dissatisfied.
- Which product journeys create the most friction.
- Which issues repeatedly affect users.
- How user frustrations differ across competitors.
- Which product improvements should be prioritised.

**The objective of this project is to convert unstructured customer feedback into structured product intelligence that helps identify, measure and prioritise user experience problems.**

## 2. Project Objectives

1. Collect publicly available Google Play reviews from 30 consumer applications in India.
2. Build an automated pipeline to clean, process and classify customer feedback.
3. Identify recurring product experience themes using AI-powered review tagging.
4. Develop a transparent, severity-weighted App Experience Index.
5. Benchmark applications within comparable product categories.
6. Build an interactive PM Copilot that converts customer feedback into product improvement opportunities.
7. Translate quantitative findings into actionable product recommendations and detailed case studies.

## 3. Applications Covered

The project covers 30 applications across six categories.

| Category | Applications | Count |
|---|---|---:|
| Fintech & Payments | PhonePe, Paytm, CRED, Groww, Zerodha Kite, BHIM | 6 |
| Quick Commerce & Food | Blinkit, Zepto, Swiggy, Zomato, BigBasket | 5 |
| Commerce & Fashion | Flipkart, Meesho, Myntra, AJIO, Tata CLiQ, Amazon | 6 |
| Beauty & Personal Care | Nykaa, Purplle, Tira, Mamaearth, Smytten | 5 |
| Mobility & Travel | Ola, Uber, Rapido, ixigo | 4 |
| AI-enabled & Content | Inshorts, Dailyhunt, ShareChat, Pocket FM | 4 |
| **Total** | **30 applications** | **30** |

## 4. Project Methodology

The project follows an end-to-end product analytics workflow.

### Step 1: Review Collection
Collect publicly accessible Google Play reviews for the selected applications, targeting approximately 500–1,000 reviews per app from the preceding 12 months, subject to availability and permitted access.

### Step 2: Data Cleaning
- Remove duplicate reviews.
- Remove extremely short or unusable feedback.
- Detect review language.
- Handle English, Hindi and Hinglish feedback.
- Prepare a structured review dataset.

### Step 3: AI-Powered Review Classification

Develop a classification pipeline to identify:

- Product experience themes.
- Review sentiment.
- Issue severity.
- Recurring user pain points.

Validate automated classifications against a manually labelled review sample.

### Step 4: App Experience Index

Calculate comparable experience metrics using:

- Theme-wise review share.
- Sentiment distribution.
- Rating trends.
- Severity-weighted Pain Index.
- Category-level benchmarks.

### Step 5: Manual Product Experience Audit

Conduct structured hands-on audits of approximately 12 applications.

Evaluate dimensions such as usability, navigation, discoverability, trust, checkout, reliability and customer support where applicable.

### Step 6: PM Copilot

Build an interactive Streamlit application that allows users to:

- Select an application.
- Explore its leading user pain points.
- Read supporting customer review snippets.
- Discover competitor experience gaps.
- View RICE-ranked product opportunities.
- Generate a draft one-page Product Requirements Document (PRD).

### Step 7: User Research and Case Studies

Conduct 15–20 user interviews and develop four detailed product case studies based on research, review insights and product analysis.

## 5. Technology Stack

| Area | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Review Collection | google-play-scraper |
| Language Detection | Python language detection libraries |
| AI Classification | LLM API |
| Data Visualisation | Plotly |
| Application Development | Streamlit |
| Data Storage | CSV |
| Version Control | Git, GitHub |
| Manual Audits | Google Sheets |

## 6. Repository Structure

```text
india_app_experience_index/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
├── notebooks/
├── taxonomy/
├── audit/
├── app/
├── case_studies/
├── reports/
├── docs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## 7. Key Deliverables

| Deliverable | Description |
|---|---|
| Review Dataset | Structured Google Play review dataset |
| Review Tagging Pipeline | AI-powered feedback classification |
| App Experience Index | Transparent application scoring framework |
| Category Benchmarks | Comparative category-level insights |
| Manual Audit Framework | Structured product experience evaluation |
| PM Copilot | Interactive product intelligence dashboard |
| Four Case Studies | Deep-dive product improvement analyses |
| Final Report | Consolidated research findings and recommendations |

## 8. Data Integrity and Limitations

This project uses publicly accessible user-generated reviews and is not an official Google Play or company-sponsored benchmark.

The analysis will account for:

- Review sampling bias.
- Differences in application review volumes.
- Language detection and classification errors.
- Limited representativeness of self-selected reviews.
- Differences in application business models.
- Insufficient evidence for low-volume themes.

No unsupported product claims or fabricated review statistics will be used.

Review collection will respect applicable platform terms and access restrictions. Unnecessary personal information will not be retained or published.

## 9. Project Status

**Current Status: Foundation & Repository Setup**

| Component | Status |
|---|---|
| Application selection | Completed |
| Repository setup | In progress |
| Review collection | Not started |
| Data cleaning | Not started |
| AI review classification | Not started |
| Experience Index | Not started |
| Manual audit | Not started |
| PM Copilot | Not started |
| User interviews | Not started |
| Case studies | Not started |
| Final publication | Not started |

## 10. Project Vision

The long-term vision is to build a consumer app intelligence platform that bridges the gap between customer feedback and product decision-making.

Rather than treating app reviews as isolated ratings, this project aims to transform them into measurable product insights that help teams understand user frustrations, identify opportunities and make evidence-based product decisions.

---

**Built as an independent Product Management and Analytics portfolio project.**
