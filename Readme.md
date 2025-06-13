# 🛡️ Loan Fraud Detection Pipeline

A scalable pipeline that detects potentially fraudulent or incomplete commercial loan applications by validating OCR-extracted documents, checking for inconsistencies (e.g., income mismatch, address mismatches), and surfacing issues via a real-time dashboard and analytics layer.

![Sample Dashboard Output](app/output.png)

---

## 📚 Contents

- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run Locally](#how-to-run-locally)
- [Architecture](#architecture)
- [Fraud Detection Rules](#fraud-detection-rules)
- [Sample Query in Redshift](#sample-query-in-redshift)

---

## 🔧 Technologies Used

### 🐍 Backend & Processing

- **Python** – Core logic and validation pipeline
- **spaCy** – NLP for address similarity
- **pandas** – Data transformation and handling
- **psycopg2 / SQLAlchemy** – PostgreSQL & Redshift integration
- **boto3** – AWS SDK (S3, Glue, Redshift)

### ☁️ AWS Stack

- **Amazon S3** – Data lake for raw loan documents
- **AWS Glue** – Metadata extraction
- **Amazon Redshift Serverless** – Analytical storage + querying
- **Amazon Athena** – Serverless S3 SQL interface
- **IAM** – Role-based permissions (Redshift ↔ S3)

### 📊 Visualization

- **Streamlit** – Dashboard to explore flagged applications
- **Redshift Query Editor v2** – Ad-hoc SQL analytics

---

## 📁 Project Structure

```bash
loan-fraud-pipeline/
├── app/
│   ├── main.py             # Entry point
│   ├── redshift.py         # Redshift query functions
│   ├── validation.py       # Fraud rules (e.g., income mismatch)
│   ├── nlp_utils.py        # spaCy-based address checks
│   ├── config.py           # Env var loader
│   └── output.png          # Sample dashboard image
├── data/
│   └── sample_outputs/     # Optional results
├── requirements.txt
├── .env
└── README.md
```
