#!usr/bin/env python3

#This is a single line comment
#python program to run lists
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 16th Feb 2023
#File : list_fruit.py
names = ["Wachira","Mary","John"]

fruits = [ "mango", "oranges", "guavas", "bananas", "melon","kiwi","apple"]
print(fruits[0:-6])
print(" My favourite fruit is:",(fruits[-6]. upper()))
#Adding two list
vegetables = ["kales", "spinach","cabbage", "managu", "brocoli"]
stationary = ["pens", "ink", "paper", "glue", "scissors"]
shopping = vegetables + stationary
print(shopping)
print(shopping[-5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shopping:
    print(shopping)
print( "My name is "+" " +names [0]+" "+ " and my favourite fruit is"+  " " + fruits [-5] )