
# 🛡️ **Loan Fraud Detection Pipeline**

A production-ready pipeline for detecting **fraudulent or incomplete commercial loan applications**. It validates OCR-extracted documents, checks for inconsistencies (e.g., income mismatch, falsified addresses), and surfaces risks via real-time analytics dashboards.

---

## 🔧 **Technologies Used**

### 🐍 Backend & Data Processing

* **Python** – Core pipeline logic and orchestration
* **spaCy** – NLP for address verification and entity extraction
* **pandas** – Data wrangling and tabular processing
* **psycopg2 / SQLAlchemy** – PostgreSQL interaction
* **boto3** – AWS SDK for S3/Glue integration

### ☁️ AWS Stack

* **Amazon S3** – Loan document storage (CSV, JSON)
* **AWS Glue** – Schema crawler & optional ETL
* **Amazon Athena** – Serverless SQL over S3
* **Amazon Redshift Serverless** – Analytics warehouse
* **IAM** – Role-based access control

### 📊 Visualization

* **Amazon Redshift Query Editor v2** – SQL exploration/debugging
* **Streamlit** – Interactive dashboards

---

## 📁 **Project Structure**

```text
loan-fraud-pipeline/
├── app/
│   ├── main.py              # Entry point
│   ├── redshift.py          # Redshift query helpers
│   ├── validation.py        # Fraud logic (e.g., income mismatch)
│   ├── nlp_utils.py         # Address NLP checks (spaCy)
│   └── config.py            # Env and credential loading
├── data/
│   └── sample_outputs/      # Mock output examples
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ **Running Locally**

### 1. Clone the Repo

```bash
git clone https://github.com/sarahschoonmaker/loan-fraud-pipeline.git
cd loan-fraud-pipeline
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Configure Environment Variables

Create a `.env` file with:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=loan_fraud
DB_USER=postgres
DB_PASSWORD=yourpassword

AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_REGION=your-region
```

### 4. Run the Pipeline

```bash
python app/main.py
```

---

## 🏗️ **Architecture Overview**

```text
                ┌────────────┐
                │ Loan CSVs  │
                │   (S3)     │
                └────┬───────┘
                     │
     ┌───────────────▼───────────────┐
     │      AWS Glue Crawler         │
     │   Extract schema from S3      │
     └──────────────┬────────────────┘
                    │
     ┌──────────────▼────────────┐
     │ Athena / Redshift Queries │◄────────────┐
     └──────────────┬────────────┘             │
                    │                          │
     ┌──────────────▼────────────┐             │
     │   Python Validation Layer │             │
     │ - Income comparison       │             │
     │ - NLP address match       │             │
     └───────────────────────────┘             │
                    │                          │
        ┌───────────▼─────────────┐            │
        │  Dashboard (Streamlit)  │◄────────────┘
        └─────────────────────────┘
```

---

## ✅ **Fraud Detection Rules**

* **Income mismatch** – >30% difference between declared and OCR-derived income
* **Address mismatch** – Fuzzy match score < 80% between OCR and provided address
* **Invalid ZIP/Location** – Zip doesn't match city/state via NLP or geodata
* **Missing fields** – Required values absent in OCR results

---

## 🔍 **Sample Query (Redshift)**

```sql
SELECT loan_id, business_name
FROM loan_applications
WHERE ABS(income - doc_income) > income * 0.3;
```

