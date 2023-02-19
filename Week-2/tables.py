#!usr/bin/env python3
#This is a single line comment
#python program to create tables
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 16th Feb 2023
#File : tables.py

#create a table
from prettytable import Prettytable
mytable = PrettyTable()

mytable.add_column(columns[0],["Jayden Wachira","Purity Muhenia","Bennedict Mwaura","Michael Murithi",])

mytable.addcolumns(columns[1],[1,2,3,4])

mytable.add_column(columns[2],["City hall","Garden city","Gotham city","Metropolitan"])

print(mytable)

