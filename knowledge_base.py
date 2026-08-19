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
- 3 years of experience building production data pipelines and ML systems.
- Actively seeking: full-time roles in Data Engineering, Data Analytics, and AI/ML Engineering
  (target titles: Data Engineer, Data Analyst, AI/ML Engineer, Python Developer),
  open to hybrid and remote roles across the US.

EXPERIENCE

Data Engineer, AI Cloud Solutions (Aug 2024 - Present)
- Building and maintaining production ETL/ELT pipelines for a finance-sector client
  across Databricks, Snowflake, and dbt, with Kafka-based streaming ingestion and
  Airflow orchestration.
- Working in a Delta Lake architecture across AWS and Azure.
- This is client work under confidentiality - do not cite specific performance
  metrics or percentages for this role (no "X% faster", "X% improvement" type
  numbers). Keep it scope/stack-level only.

Data Analyst Intern, FoxFire Technologies (Jan 2021 - Dec 2021)
- Optimized data extraction scripts and ETL processes from relational databases,
  reducing report generation latency by 15%.
- Built operational dashboards in Tableau and Power BI for supply chain and
  inventory visibility.
- Developed an automated data quality framework using SQL and Python with
  statistical anomaly detection.
- Conducted root-cause analyses on pipeline discrepancies using hypothesis testing.

EDUCATION
- Master's, Data Science & Artificial Intelligence - Florida International University
  (2022 - 2024), Miami, FL.

TECHNICAL SKILLS (full list)
- Programming: Python, SQL, R, Java, C/C++
- Data Engineering: Apache Spark, PySpark, Airflow, Kafka, ELT/ETL,
  Kimball/Dimensional modeling, Delta Lake
- Cloud: AWS (S3, EC2, IAM, Redshift), Kubernetes, Docker, Azure, GCP
- Data Warehousing: Snowflake, Databricks (Unity Catalog), dbt, PostgreSQL, Redshift
- Visualization/Tools: Power BI, Tableau, Looker, Git, GitHub, Jenkins, CI/CD
- ML/Analytics: Feature Engineering, NumPy, pandas, scikit-learn, Statistical
  Methods, FastAPI
- Also used in projects: XGBoost, Random Forest, HuggingFace Transformers, BART,
  FinBERT, matplotlib, SQLAlchemy

AT A GLANCE
- 3 years experience
- 4 GitHub projects
- 3 live deployments

PROJECTS (4 total, all on the Projects page of the site)

1. Fraud Detection Pipeline & ML System
   - Processes 284,807 real credit card transactions (0.17% fraud rate).
   - PySpark ETL pipeline, genuinely orchestrated with Apache Airflow - a real DAG
     (ingest -> transform -> train) has been run end-to-end successfully.
   - Data genuinely flows through PostgreSQL before transformation: Spark reads the
     transaction data via JDBC from Postgres, not directly from a CSV.
   - Trained and compared Random Forest and XGBoost classifiers.
   - Random Forest is the version deployed to production: 0.9839 ROC-AUC, 83% recall,
     77% precision on 56,962 held-out transactions.
   - XGBoost was also trained (84% recall, 89% precision) but is not the deployed model.
   - 5 engineered features: log-normalized amount, rolling transaction velocity,
     rolling average amount, transaction hour, and a high-value flag.
   - Served via a FastAPI REST endpoint, containerized with Docker, and genuinely
     deployed and running on a local Kubernetes cluster (a Deployment + Service,
     with verified running pods).
   - Processed Parquet output is genuinely written to AWS S3.
   - Measured latency is a real benchmark, not an estimate: p50 ~299ms, p95 ~475ms,
     mean ~344ms. Cite this as "median response time of about 300ms" - never as
     "under 200ms," which was an old, superseded estimate.
   - Why it matters: with only a 0.17% fraud rate in the data, plain accuracy is the
     wrong metric (predicting "legitimate" for everything scores 99.83% accuracy
     while catching zero fraud) - ROC-AUC and recall are the right metrics here.
   - GitHub: github.com/anirudhcancode/fraud-detection-pipeline
   - Live demo page: fraud-demo.html on the site
   - Live API: https://fraud-detection-pipeline-p6mq.onrender.com/docs

2. LLM Financial Report Analyzer / Intelligence Platform
   - Reads, summarizes, and scores the sentiment/tone of financial earnings reports.
   - NLP core: BART (facebook/bart-large-cnn) for summarization, FinBERT
     (ProsusAI/finbert) for financial sentiment, and YAKE for keyword extraction.
   - Correctly identified Apple as the only negative report in its test set, at
     94.88% confidence.
   - Extended "Intelligence Platform" build adds: 10 years of price history for 10
     real stock tickers via yfinance, 28,877 price records, 454 earnings records, a
     GradientBoosting model for directional predictions, and 14 interactive Plotly
     charts.
   - The deployed live API serves the core sentiment/summary/company-comparison
     functionality. The extended endpoint set (stock history, predictions,
     correlation) was built and validated locally but is not part of the live
     deployed API - it was scaled back for free-tier hosting reliability.
   - GitHub: github.com/anirudhcancode/llm-financial-analyzer
   - Demo pages: llm-demo.html, and an extended demo at llm-intelligence-demo.html
   - Live demo hosted on Render.

3. A/B Testing & Experimentation Pipeline
   - Simulates an e-commerce checkout flow A/B test: 10,000 synthetic users over a
     14-day period. This is a synthetic/seeded dataset, not live production traffic.
   - Uses a z-test for statistical significance, confidence intervals, and lift
     metrics.
   - Results: 26% conversion lift, p-value of 0.000007.
   - FastAPI REST API backed by PostgreSQL, with on-demand simulation.
   - GitHub: github.com/anirudhcancode/ab-testing-pipeline
   - Live demo page: ab-demo.html on the site, hosted on Render.

4. AI Companion (In Development - private repo)
   - Cross-platform AI assistant for iOS, Android, and web, built with React
     Native/Expo.
   - Node/Express backend, a tool-orchestrated Claude reasoning loop, and semantic
     memory via pgvector.
   - Live integrations: health, music, weather, news, and web search.
   - The conversation engine, memory system, and emotional calibration are live and
     in daily use; the visual/theming layer is still evolving.
   - Includes user-controlled data privacy: users can export data, delete memories,
     and clear history.
   - Premise: a presence that doesn't leave, whoever the user turns out to be. Two
     layers - tool-orchestrated reasoning that decides what context a moment calls
     for, and a memory system that earns the right to go deeper over time rather
     than assuming it.
   - Still in development. Repo is private.
   - Learn-more page: ai-companion-demo.html on the site.

CONTACT / GETTING IN TOUCH
For anything Krypto can't answer - personal questions, hiring inquiries,
collaboration requests, or questions about how Krypto itself was built - direct
people to:
- LinkedIn: linkedin.com/in/anirudhravipudi
- Email: anirudhravipudi@outlook.com
- GitHub: github.com/anirudhcancode
- The portfolio's Contact page also has a working contact form.
- Resume is available on the About page of the site.

SITE STRUCTURE
The portfolio has four main pages: Home, Projects, About, and Contact, plus individual
live-demo pages for each project (fraud-demo.html, llm-demo.html, llm-intelligence-demo.html,
ab-demo.html, ai-companion-demo.html).
"""
