#!usr/bin/env python3

#This is a single line comment
#python program on numbers
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 14th Feb 2023
#File : numbers.py

numbers = [6]

sum_num = 0
for number in numbers:
    number = int(input("Enter the number :"))
    sum_num = sum_num + number
    avg_num = sum_num / 10
    print(avg_num)