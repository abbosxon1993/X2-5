import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="yusername",
      passwd="password",
      database="database_name"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")

mycursor.execute("INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')")
mydb.commit() # Use this command after insert, update, delete commands
