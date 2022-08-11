import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="music",
    user="postgres",
    password="yasar",
    port="5432"
)

cursor = conn.cursor()