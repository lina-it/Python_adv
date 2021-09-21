import psycopg2
from sys import argv

print(argv)
DB_URL = 'postgresql://postgres:1111@127.0.0.1:5432/postgres'

CREATE_TABLE_QUERY = """CREATE TABLE users(
user_id serial PRIMARY KEY NOT NULL,
username text,
is_subscribed VARCHAR(30) NOT NULL
)"""

INSERT_TABLE_QUERY = """INSERT INTO users (username, is_subscribed) VALUES (%s,%s)"""
data_users = [
    ('TONY STARK', 'True'),
    ('TIM ADOLF', 'False'),
    ('KIM JARVIS', 'True'),
    ('SAM MILES', 'True'),
    ('KEVIN HILL', 'False')
]

SELECT_CHECK_ACTIVE = """SELECT * FROM users where is_subscribed ='True';"""
SELECT_CHECK_FALSE = """SELECT * FROM users where is_subscribed ='True';"""
Update = """UPDATE users SET is_subscribed = 'False' where user_id = (%s)"""
conn = psycopg2.connect(DB_URL)
with conn.cursor() as cursor:
    cursor.execute(CREATE_TABLE_QUERY)

    cursor.executemany(INSERT_TABLE_QUERY, data_users)
    conn.commit()

    cursor.execute(SELECT_CHECK_ACTIVE)
    # cursor.execute(Update % (input("d: ")))
    # conn.commit()
    cursor.execute(SELECT_CHECK_FALSE)
    print(cursor.fetchall())