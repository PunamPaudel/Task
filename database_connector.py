import mysql.connector


# connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print("Connected successfully!")

mycursor = mydb.cursor()

mycursor.execute("")

for x in mycursor:
    print(x)
