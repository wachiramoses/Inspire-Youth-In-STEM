#!usr/bin/env python3

#This is a single line comment
#python program to calculate tax and gross income
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 17th Feb 2023
#File : bank.py

#write a program that calculate 16% per income
#ranging between 100k - 150k

#9% tax income is between 150k - 300k
#30% tax income is above 300k
#5% if income is less 100k

#print gross income ,net income
gross_income =int(input("what is your gross income "))
tax_group_1 = (gross_income * 0.05)
tax_group_2 = (gross_income * 0.16 )
tax_group_3 = (gross_income * 0.19)
tax_group_4 = (gross_income * 0.3)

if gross_income < 100000:
    print("gross income:", gross_income)
    print("net income ", gross_income - tax_group_1)

elif (gross_income > 100000) & (gross_income < 150000):
    print("gross_income",gross_income)
    print("net_income:", gross_income - tax_group_2)

elif(gross_income <=150001) & (gross_income <100000):
    print("gross_income = ",gross_income)
    print("tax = ",(gross_income - tax_group_3))
    print("net_income:", gross_income - tax_group_3)

else:
    ("gross_income",gross_income)
    print("net_income:", gross_income - tax_group_4)


