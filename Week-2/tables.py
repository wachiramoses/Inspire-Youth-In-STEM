#!usr/bin/env python3
#This is a single line comment
#python program to create tables
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 16th Feb 2023
#File : tables.py

#import module
from tabulate import tabulate

#assign data
mydata = [
    ["Wachira"   ,   "Nyeri"] ,
    ["Fatuma"   ,   "Mombasa"] ,
    ["Odinga"   ,   "Kisumu"] ,
    ["Kipkoech"   ,   "Uasin Gishu"] ,
    ["Wafula"   ,    "Bungoma"] ,
    ["Muthuri"   ,   "Meru"] ,
]
#create header
head = [ "Name"   ,   "County" ]

#display table
print(tabulate(mydata , headers = head, tablefmt = "grid"))