# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('test1.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255), Mark INT);"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Shishir', 'Data Science', 'A','22')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ram', 'Data Science', 'B','99')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('krish', 'Devops', 'C','55')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('siddhu', 'Data Science', 'C','33')''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()