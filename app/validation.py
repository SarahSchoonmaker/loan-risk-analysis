def detect_income_mismatch(record):
    try:
        declared = float(record["income"])
        documented = float(record["doc_income"])
        if abs(declared - documented) / declared > 0.3:
            return True
    except:
        return False

def detect_missing_fields(record):
    return any(record.get(k) in (None, '', 'NULL') for k in ["income", "doc_income", "address", "doc_address"])
