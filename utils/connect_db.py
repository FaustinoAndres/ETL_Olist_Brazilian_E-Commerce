import psycopg2
from decouple import config

try:
    conn = psycopg2.connect(
        host = config('HOST'),
        database = config('DATABASE'),
        user = config('USER'),
        password = config('PASSPORT')
        )

    print("Successful connection")
    #cursor = conn.cursor()
    #row = cursor.fetchone()
    #print(row)

except Exception as ex:
    print(ex)