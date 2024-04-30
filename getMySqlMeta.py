import mysql.connector

mydb = mysql.connector.connect(
  host="54.162.42.172",
  user="stockairo",
  password="make-sql-from-text-4-all",
  database="svday_etfdb"
)

# Check connection
if mydb.is_connected():
    print("Connection successful.")

# Create a cursor object for SQL operations
mycursor = mydb.cursor()

# Example of executing a query
mycursor.execute("SELECT * FROM information_schema.columns WHERE table_schema = 'svday_etfdb' ")

# Fetch results (if applicable)
for row in mycursor:
    print(row)

# Close the connection 
mydb.close()