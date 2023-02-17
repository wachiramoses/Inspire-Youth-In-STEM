#!usr/bin/env python3

#This is a single line comment
#python program to create tables
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 16th Feb 2023
#File : assignment.py

import sqlite3

#connect to sqlite
conn sqlite3.connect('example.db')

#creating a cursor object using the cursor() method
cursor = conn.cursor()

#doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per employee
sql ='''CREATE A TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT
)'''
cursor.execute(sql)
print("Table created successfully........")
#commit your changes in the database
conn.commit()

#closing the connection
conn.close


