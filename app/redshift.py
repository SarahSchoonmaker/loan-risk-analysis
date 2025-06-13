import psycopg2
from config import *

def fetch_loan_data():
    conn = psycopg2.connect(
        dbname=REDSHIFT_DB,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM loan_applications")
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    conn.close()
    return [dict(zip(headers, row)) for row in rows]
