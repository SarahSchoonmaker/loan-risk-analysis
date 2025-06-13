import streamlit as st
from redshift import fetch_loan_data
from validation import detect_income_mismatch, detect_missing_fields
from nlp_utils import is_address_suspect

st.set_page_config(page_title="Loan Fraud Dashboard", layout="wide")
st.title("🚨 Loan Fraud Detection Dashboard")

# Load loan records
data = fetch_loan_data()

flagged = []
for record in data:
    reasons = []
    if detect_income_mismatch(record):
        reasons.append("Income mismatch")
    if detect_missing_fields(record):
        reasons.append("Missing fields")
    if is_address_suspect(record["address"], record["doc_address"]):
        reasons.append("Address mismatch")

    record["flagged"] = bool(reasons)
    record["reasons"] = ", ".join(reasons)
    flagged.append(record)

# Streamlit UI
st.markdown(f"### Total Loans: {len(flagged)}")
st.markdown(f"### 🚩 Flagged Loans: {sum([r['flagged'] for r in flagged])}")

# Filter toggle
show_only_flagged = st.checkbox("Show only flagged loans", value=True)

filtered = [r for r in flagged if r["flagged"]] if show_only_flagged else flagged

# Show table
st.dataframe(filtered, use_container_width=True)
