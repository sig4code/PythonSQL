# Mairadb connector with python

How to connect to a mariadb or mysql database

Imports needed:

```python 
import mysql.connector as mariadb
```

Create Connetion object:

```python 
mariadb_connection = mariadb.connect(user='homelab', password='********', host='localhost', port='3306')
```

define cursor:

```python 
create_cursor = mariadb_connection.cursor()   # dictionary = True
```
some queries:

```python
## SQL QUERy Table output
sql_statement = 'USE homelabdb'
create_cursor.execute(sql_statement)

sql_statement = 'SELECT * FROM KUNDEN'
create_cursor.execute(sql_statement)
#result = create_cursor.fetchone()
result = create_cursor.fetchall()
print(result)
```


close connection
```python
mariadb_connection.close()
```
