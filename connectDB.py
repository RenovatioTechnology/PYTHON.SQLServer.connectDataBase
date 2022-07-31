import mysql.connector

mydb = mysql.connector.connect(
    # url for database
    host='localhost',
    user='root',
    passwd='pwd1235',
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
# my_cursor.execute('SHOW TABLES')
#   print(table)

# Add/ INSERT records into table #
# sqlInfo = 'INSERT INTO user (name, email, age) Value (%s, %s, %s)'
# record1 = ('Jeff', 'jeff@renovatio3d.com', 39)
# my_cursor.execute(sqlInfo, record1)
# commit changes #
# mydb.commit()

# INSERT Multiple records into table #
sqlInfo = 'INSERT INTO user (name, email, age) Value (%s, %s, %s)'
records = [
    ('Steve', 'steve@yahoo.com', 38),
    ('Tina', 'tina@aol.com', 21),
    ('Eric', 'eric@live.com', 37),
    ('Jessica', 'jessica@gmail.com', 28), ]
my_cursor.executemany(sqlInfo, records)
mydb.commit()
