import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=test user=postgres")
# conn = psycopg2.connect(
#     host="localhost",
#     database="suppliers",
#     user="postgres",
#     password="Abcd1234")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM my_data")

# Retrieve query results
records = cur.fetchall()