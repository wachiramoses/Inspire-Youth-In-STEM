#!usr/bin/env python3
#This is a single line comment
#python program to list all prime_odd_even numbers from 1-100
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 15th Feb 2023
#File : prime_odd_even.py

#write a program to list all odd numbers from 1-100
print("***The values below are odd numbers***")
for odd_numbers in range(1,101):
    if(odd_numbers%2 != 0):
        print(odd_numbers)

#write a program to list all even numbers from 1-100
print("***The values below are even numbers***")
for even_numbers in range(1,101):
    if(even_numbers%2 == 0):
        print(even_numbers)

#write a program to list all prime numbers from 1-100
print("***The values below are prime numbers***")
for prime_numbers in range(1, 101):
   if prime_numbers > 1:
       for i in range(2, prime_numbers):
           if (prime_numbers % i) == 0:
                    break
       else:
           print(prime_numbers)

#write a program to calculate arithmetic progression of numbers from 1-20
#formula n = nth term in the sequence,a = first term,d = common difference(was not given,random)
#AP=a+(n-1)d
nth_term = 20
first_term = 1

common_difference = input("What's the common difference:(should be < 9) ")
if (int(common_difference) > 9):
        print("Out of range!!!")
else:
    arithmetic_progression = first_term + ((nth_term - 1) * int(common_difference))
    print("The arithmetic progression is:",arithmetic_progression)










