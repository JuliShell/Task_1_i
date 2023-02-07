#!/usr/bin/env python
# coding: utf-8

# In[4]:


import psycopg2
import psycopg2.extras as extras
import pandas as pd

a = pd.read_json('/Users/shell/Desktop/Innowise/Task_1_data/students.json')
print(a)

def execute_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = ','.join(list(df.columns))
    
 # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_values() done")
    cursor.close()

# establishing connection
conn = psycopg2.connect(
    database="Task_1",
    user='postgres',
    password='2206',
    host='localhost',
    port='5432'
)
sql = '''CREATE TABLE students_data (birthday date, id int, name char(40), room int, sex char(6));'''

# creating a cursor
cursor = conn.cursor()
cursor.execute(sql)
data = pd.read_json('/Users/shell/Desktop/Innowise/Task_1_data/students.json')  
data = data[["birthday", "id", "name", "room", "sex"]]

# using the function defined
execute_values(conn, data, 'students_data')
  
    


# In[5]:


import psycopg2
import psycopg2.extras as extras
import pandas as pd

a = pd.read_json('/Users/shell/Desktop/Innowise/Task_1_data/rooms.json')
print(a)

def execute_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = ','.join(list(df.columns))
    
 # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_values() done")
    cursor.close()

# establishing connection
conn = psycopg2.connect(
    database="Task_1",
    user='postgres',
    password='2206',
    host='localhost',
    port='5432'
)
sql = '''CREATE TABLE rooms_data (id int, name char(50));'''

# creating a cursor
cursor = conn.cursor()
cursor.execute(sql)
data = pd.read_json('/Users/shell/Desktop/Innowise/Task_1_data/rooms.json')  
data = data[["id", "name"]]

# using the function defined
execute_values(conn, data, 'rooms_data')
  


# In[ ]:




