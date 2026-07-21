import psycopg

conn_string = "dbname=bank user=postgres password=1292 host=localhost port=5432"

try:
    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print("Connected successfully! PostgreSQL version:", db_version[0])
except Exception as e:
    print("Failed to connect:", e)