import psycopg2
from psycopg2 import connect
from decouple import config

def connect_to_db() -> connect:

    return psycopg2.connect(
        host = config('HOST'),
        database = config('DATABASE'),
        user = config('USER'),
        password = config('PASSWORD')
        )

