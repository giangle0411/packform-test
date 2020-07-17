from psycopg2 import connect, extensions

# Create a new postgreSQL database

conn = connect(
    "host=localhost dbname=postgres user=postgres password=postgres")
# get the isolation leve for autocommit
autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# set the isolation level for the connection's cursors
conn.set_isolation_level(autocommit)

cur = conn.cursor()

DB_NAME = "orders_details"
cur.execute('CREATE DATABASE ' + str(DB_NAME))
