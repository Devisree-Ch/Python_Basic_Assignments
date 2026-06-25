# Get the top 5 products by revenue.
import sqlite3

conn=sqlite3.connect("Revenue.db")
cur=conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS Products(
# 	product_id INTEGER,
# 	product_name TEXT,
# 	revenue INTEGER)""")
# cur.execute("INSERT INTO Products VALUES(1,'earphones',5)")
# cur.execute("INSERT INTO Products VALUES(1,'buds',6)")
# cur.execute("INSERT INTO Products VALUES(1,'pouches',7)")
# cur.execute("INSERT INTO Products VALUES(1,'mobilephones',10)")
# cur.execute("INSERT INTO Products VALUES(1,'laptops',20)")
# cur.execute("INSERT INTO Products VALUES(1,'keyboard',25)")
# cur.execute("INSERT INTO Products VALUES(1,'mouse',45)")
# cur.execute("INSERT INTO Products VALUES(1,'chargers',35)")
# cur.execute("INSERT INTO Products VALUES(1,'cables',60)")
# cur.execute("INSERT INTO Products VALUES(1,'modem',50)")
# cur.execute("INSERT INTO Products VALUES(1,'wifi',54)")

# conn.commit()

# cur.execute("SELECT DISTINCT product_name,revenue from Products ORDER BY revenue DESC LIMIT 5")
# print(cur.fetchall())
# ===================================================================================================================
# List customers who purchased more than 10 times.
# import sqlite3
# conn=sqlite3.connect("Customer.db")
# cur=conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS Customer(
# 	customerid INTEGER PRIMARY KEY,
# 	product_name TEXT,
# 	cname TEXT)""")
# cur.execute("PRAGMA table_info(Customer)")
# print(cur.fetchall())
# cur.execute("SELECT * from Customer")
# print(cur.fetchall())
# cur.execute("""ALTER TABLE Customer DROP Column customers""")
# cur.execute("INSERT INTO Customer VALUES(1,'wifi','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(2,'modem','Anu')")
# cur.execute("INSERT INTO Customer VALUES(3,'wifi','Sourav')")
# cur.execute("INSERT INTO Customer VALUES(4,'modem','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(5,'wifi','Virat')")
# cur.execute("INSERT INTO Customer VALUES(6,'earphones','Nami')")
# cur.execute("INSERT INTO Customer VALUES(7,'buds','Suba')")
# cur.execute("INSERT INTO Customer VALUES(8,'pouches','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(9,'mobilephones','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(10,'laptops','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(11,'earphones','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(12,'buds','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(13,'pouches','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(14,'mobilephones','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(15,'laptops','Amrita')")
# cur.execute("INSERT INTO Customer VALUES(16,'laptops','Amrita')")
# conn.commit()
# cur.execute("SELECT cname,count(*) from Customer GROUP BY cname HAVING count(*)>=10")
# print("Customer with more than 10 orders",cur.fetchall())
# =====================================================================================
# Find the month with the highest sales.
# Find products that were never sold.
# Get total sales per region.
# Find the top customer in each region.
# Total sales per product
# Count of employees per department
# Average salary per job role
# Rank employees by salary within each department
# Find cumulative sales per customer
# Get the top 3 highest-paid employees overall
# Find the total sales amount per customer.