import csv
import psycopg2
conn = psycopg2.connect(
    "host=localhost dbname=orders_details user=postgres password=postgres")

cur = conn.cursor()

# Create postgreSQL database's tables

cur.execute("""CREATE TABLE deliveries(
    id integer PRIMARY KEY,
    order_item_id integer,
    delivered_quantity integer
)
""")
conn.commit()

cur.execute("""CREATE TABLE order_items(
    id integer PRIMARY KEY,
    order_id integer,
    price_per_unit float,
    quantity integer,
    product text
)
""")
conn.commit()

cur.execute("""CREATE TABLE orders(
    id integer PRIMARY KEY,
    created_at date,
    order_name text,
    customer_id text
)
""")
conn.commit()

# Write .csv file data into PosgreSQL database with according tables

with open("..\database\Test task - Postgres - deliveries.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        values = ','.join(["'" + str(i) + "'" if i else 'NULL' for i in row])
        cur.execute('insert into deliveries VALUES ({});'.format(values))
        conn.commit()
conn.commit()

with open("..\database\Test task - Postgres - order_items.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        values = ','.join(["'" + str(i) + "'" if i else 'NULL' for i in row])
        cur.execute('insert into order_items VALUES ({});'.format(values))
        conn.commit()
conn.commit()

with open("..\database\Test task - Postgres - orders.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        values = ','.join(["'" + str(i) + "'" if i else 'NULL' for i in row])
        cur.execute('insert into orders VALUES ({});'.format(values))
        conn.commit()
conn.commit()
