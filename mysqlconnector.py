#!/usr/bin/python3

import mysql.connector as mariadb

## create mysql connection and define cursor:
mariadb_connection = mariadb.connect(user='homelab', password='homelab', host='localhost', port='3306')

create_cursor = mariadb_connection.cursor()   # dictionary = True

create_cursor.execute("SHOW DATABASES") 
for database in create_cursor:
   print(database)


## SQL QUERy Table output
sql_statement = 'USE homelabdb'
create_cursor.execute(sql_statement)
sql_statement = 'SELECT * FROM KUNDEN'
create_cursor.execute(sql_statement)
#result = create_cursor.fetchone()
result = create_cursor.fetchall()
print(result)



## close connection
mariadb_connection.close()

