import mysql.connector

mydb = mysql.connector.connect(
    # url for database
    host='localhost',
    user='root',
    passwd='pwd1235!',
    database='testdb',
)
my_cursor = mydb.cursor()
# execute command, create database
# my_cursor.execute('CREATE DATABASE testdb')

# Check if database exist, show them all in the cursor #
# my_cursor.execute('SHOW DATABASES')
# for db in my_cursor:
# print(db[0])

# Create a table, with columns #
# my_cursor.execute('CREATE TABLE user(name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)')
# test above table
my_cursor.execute('SHOW TABLES')
for table in my_cursor:
    print(table)
