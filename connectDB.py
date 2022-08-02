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
# sqlInfo = 'INSERT INTO user (name, email, age) Value (%s, %s, %s)'
# records = [
# ('Steve', 'steve@yahoo.com', 38),
# ('Tina', 'tina@aol.com', 21),
# ('Eric', 'eric@live.com', 37),
# ('Jessica', 'jessica@gmail.com', 28), ]
# my_cursor.executemany(sqlInfo, records)
# mydb.commit()

# Pulling data from database #
# my_cursor.execute('SELECT * FROM user')
# fetchAll = my_cursor.fetchall()
# Header
# print('NAME\t\tEMAIL\t\tAGE\tID')
# Diving line
# print('____\t\t_____\t\t___\t__')
# for row in fetchAll:
# Readable report placeholder
#   print(row[0] + '\t %s' % row[1] + '\t%s' % row[2] + '\t%s' % row[3])

# WHERE Clause, finding all specific search
# my_cursor.execute("SELECT * FROM user WHERE name = 'Jeff'")
# my_cursor.execute('SELECT * FROM user WHERE age > 30')
# fetchAll = my_cursor.fetchall()
# for row in fetchAll:
#  print(row)

# LIKE Clause, finding all specific search
my_cursor.execute("SELECT * FROM user WHERE name LIKE '%i%'")
# my_cursor.execute("SELECT * FROM user WHERE name LIKE 'J%'")
# my_cursor.execute('SELECT * FROM user WHERE age > 30')
fetchAll = my_cursor.fetchall()
for row in fetchAll:
    print(row)
