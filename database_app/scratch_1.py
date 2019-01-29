import psycopg2

# Set up connection to database with information saved in postgres
connection = psycopg2.connect(database="Learning", user="postgres", password="Shinji21", host="localhost")

cursor = connection.cursor()

cursor.execute("SELECT * FROM purchases")

for row in cursor:
    print(row)

