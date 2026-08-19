"""
Factual context about Anirudh Ravipudi, sourced directly from
anirudhcancode.github.io/portfolio. Krypto is only allowed to answer
using what's in here — nothing invented, nothing assumed.
"""

KNOWLEDGE_BASE = """
IDENTITY
- Name: Anirudh Ravipudi
- Title: Data Engineer
- Location: New York City, NY
- Actively seeking: full-time roles in Data Engineering, Data Analytics, and AI/ML Engineering
  (target titles: Data Engineer, Data Analyst, AI/ML Engineer, Python Developer),
  open to hybrid and remote roles across the US.

CURRENT ROLE
- Data Engineer at AI Cloud Solutions (Aug 2024 - Present)
- Building and maintaining production ETL/ELT pipelines for a finance-sector client
  across Databricks, Snowflake, and dbt, with Kafka-based streaming ingestion and
  Airflow orchestration. Working in a Delta Lake architecture across AWS and Azure.

EDUCATION
- Master's, Data Science & AI - Florida International University (2022 - 2024)
- Bachelor's, Information Technology - undergraduate studies (2018 - 2022)

PRIOR EXPERIENCE
- Data Analyst Intern at FoxFire Technologies (Jan 2021 - Dec 2021)

CORE TECH STACK
Python, SQL, PySpark, Apache Airflow, Docker, AWS, PostgreSQL, Databricks, Snowflake, FastAPI.
Also: scikit-learn, XGBoost, Random Forest, HuggingFace Transformers, BART, FinBERT,
pandas, NumPy, scipy, Power BI, Tableau, matplotlib, SQLAlchemy, Kubernetes, Azure.

AT A GLANCE
- 3+ years experience
- 4 GitHub projects
- 3 live deployments

PROJECTS (4 total, all on the Projects page of the site)

1. Fraud Detection Pipeline & ML System
   - End-to-end fraud detection system processing 284,807 real credit card transactions.
   - Built a PySpark ETL pipeline with behavioral feature engineering (rolling-window
     transaction patterns via Spark's distributed windowing).
   - Trained and compared Random Forest and XGBoost classifiers. Random Forest is the
     version currently deployed, served via a FastAPI REST endpoint containerized with Docker.
   - Results: Random Forest - 0.9839 ROC-AUC, 83% recall, 77% precision.
     XGBoost - 0.9827 ROC-AUC, 84% recall, 89% precision (trained/compared, not the deployed one).
   - Why it matters: with only a 0.17% fraud rate in the data, plain accuracy is the wrong
     metric (predicting "legitimate" for everything scores 99.83% accuracy while catching zero
     fraud) - ROC-AUC and recall are the right metrics here.
   - GitHub: github.com/anirudhcancode/fraud-detection-pipeline
   - Live demo page: fraud-demo.html on the site
   - Live API: https://fraud-detection-pipeline-p6mq.onrender.com/docs

2. LLM Financial Report Analyzer
   - Reads, summarizes, and scores the sentiment/tone of financial earnings reports in seconds.
   - Built with BART for summarization, FinBERT for financial sentiment, and YAKE for
     keyword extraction.
   - Correctly identified Apple as the only negative report in its test set.
   - Metrics: 94% confidence, 5 companies analyzed, 3 NLP models used.
   - GitHub: github.com/anirudhcancode/llm-financial-analyzer
   - Demo pages: llm-demo.html, and an extended "Intelligence Platform" demo at
     llm-intelligence-demo.html

3. A/B Testing & Experimentation Pipeline
   - Simulates an e-commerce checkout flow A/B test across 10,000 users over 14 days.
   - Uses a z-test for statistical significance, confidence intervals, and lift metrics,
     exposed via a REST API.
   - Results: 26% conversion lift, 10,000 users, p-value of 0.000007.
   - GitHub: github.com/anirudhcancode/ab-testing-pipeline
   - Live demo page: ab-demo.html on the site

4. AI Companion (In Development - private repo)
   - Cross-platform AI assistant (React Native, LLMs, vector search, Node.js).
   - Premise: a presence that doesn't leave, whoever the user turns out to be. Two layers:
     tool-orchestrated reasoning that decides what context a moment calls for, and a memory
     system that earns the right to go deeper over time rather than assuming it.
   - 3 platforms, 5 integrations. Repo is private.
   - Learn-more page: ai-companion-demo.html on the site

CONTACT
- Email: anirudhravipudi@outlook.com
- LinkedIn: linkedin.com/in/anirudhravipudi
- GitHub: github.com/anirudhcancode
- Typically responds within 24 hours; LinkedIn is the fastest way to reach him for
  urgent inquiries.
- Resume is available on the About page of the site.

SITE STRUCTURE
The portfolio has four main pages: Home, Projects, About, and Contact, plus individual
live-demo pages for each project (fraud-demo.html, llm-demo.html, llm-intelligence-demo.html,
ab-demo.html, ai-companion-demo.html).
"""
