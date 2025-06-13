from redshift import fetch_loan_data
from validation import detect_income_mismatch, detect_missing_fields
from nlp_utils import is_address_suspect

def main():
    records = fetch_loan_data()
    flagged = []

    for record in records:
        reasons = []
        if detect_income_mismatch(record):
            reasons.append("Income mismatch")
        if detect_missing_fields(record):
            reasons.append("Missing fields")
        if is_address_suspect(record["address"], record["doc_address"]):
            reasons.append("Address mismatch")

        if reasons:
            flagged.append({"loan_id": record["loan_id"], "reasons": reasons})

    print("🚩 Flagged Loans:")
    for loan in flagged:
        print(f"Loan {loan['loan_id']}: {', '.join(loan['reasons'])}")

if __name__ == "__main__":
    main()
