```
# 🛡️ Loan Fraud Detection Pipeline

A production-ready pipeline that detects potentially fraudulent or incomplete commercial loan applications by validating OCR-extracted documents, checking for field inconsistencies (e.g., income mismatch, falsified addresses), and surfacing issues via a real-time dashboard and analytics layer.

---

## 🔧 Technologies Used

### 🐍 Backend & Data Processing

- **Python** – Core pipeline logic and validation
- **spaCy** – NLP for address matching, entity recognition
- **pandas** – Data wrangling and transformation
- **psycopg2 / SQLAlchemy** – PostgreSQL connectivity
- **boto3** – AWS SDK for S3 and Glue integration

### ☁️ AWS Stack

- **Amazon S3** – Data lake storage for loan documents (CSV, JSON)
- **AWS Glue** – Metadata crawling and optional ETL jobs
- **Amazon Athena** – Serverless SQL for querying S3 data
- **Amazon Redshift Serverless** – Fast analytics and dashboard backend
- **IAM** – Role-based access control for S3 and Redshift

### 📊 Visualization

- **Amazon Redshift Query Editor v2** – For analytics and debugging
- **Visualization**: Streamlit

---

## 📁 Project Structure
```

loan-fraud-pipeline/
├── app/
│ ├── main.py # Entry point
│ ├── redshift.py # Redshift query functions
│ ├── validation.py # Fraud rules (e.g., income mismatch)
│ ├── nlp_utils.py # spaCy-based address checks
│ └── config.py # Env and credentials loader
├── data/
│ └── sample_outputs/ # (Optional) mock outputs
├── requirements.txt
├── .env
└── README.md

````

---

## ⚙️ How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/sarahschoonmaker/loan-fraud-pipeline.git
cd loan-fraud-pipeline
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Setup Environment Variables

Create a `.env` file:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=loan_fraud
DB_USER=postgres
DB_PASSWORD=yourpassword

AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_REGION=your_region
```

### 4. Run the Pipeline

```bash
python app/main.py
```

---

## 🏗️ Architecture

```text
                  ┌────────────┐
                  │ Loan CSVs  │
                  │ (S3)       │
                  └────┬───────┘
                       │
        ┌──────────────▼───────────────┐
        │     AWS Glue Crawler         │
        │  Extract schema from S3      │
        └──────────────┬───────────────┘
                       │
        ┌──────────────▼────────────┐
        │    AWS Athena / Redshift  │◄────────────┐
        │  SQL queries on loan data │             │
        └──────────────┬────────────┘             │
                       │                          │
     ┌─────────────────▼────────────┐             │
     │       Python Validation      │             │
     │  - Compare income fields     │             │
     │  - NLP address similarity    │             │
     └──────────────────────────────┘             │
                       │                          │
           ┌───────────▼────────────┐             │
           │    Dashboard Layer     │             │
           │  (Streamlit/QuickSight)│◄────────────┘
           └────────────────────────┘
```

---

## ✅ Fraud Detection Rules

- **Income mismatch**: difference > 30% between declared and OCR income
- **Address mismatch**: NLP fuzzy match score < threshold (e.g., 80%)
- **Invalid zip/location**: Zip doesn't match extracted address
- **Missing values**: Empty OCR fields

---

## 🔍 Sample Query in Redshift

```sql
SELECT loan_id, business_name
FROM loan_applications
WHERE ABS(income - doc_income) > income * 0.3;
```

---
