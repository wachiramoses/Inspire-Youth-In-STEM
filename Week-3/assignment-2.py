#1.write a program that calculates quadratic equation 
#2.using for loop draw a diamond,triangle, and pascals triangle

import cmath

first_coefficient = int(input("Enter the first coefficient: "))
second_coefficient = int(input("Enter the second coefficient: "))
constant = int(input("Enter the constant: "))

ans1 = -abs(second_coefficient) - cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)
ans2 = -abs(second_coefficient) + cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)

print("The answers are "+str(ans1)+" and "+str(ans2))

#using a for loop draw a diamond
R = int(input("Enter the range: "))
for diamond in range(R):
    print("  " * (R - diamond), " *" * (2 * diamond +1))
for diamond in range(R-2,-1,-1):
    print("  " * (R - diamond), " *" * (2 * diamond +1))

print("-----------------------------------------")

#using a for loop draw a triangle
for diamond in range(R):
    print("  " * (R - diamond), " *" * (2 * diamond +1))

print("------------------------------------------")

#using a for loop draw pascals triangle
for i in range(1, R+1):
	for j in range(0, R-i+1):
		print(' ', end='')

	# first element is always 1
	C = 1
	for j in range(1, i+1):

		# first value in a line is always 1
		print(' ', C, sep='', end='')

		# using Binomial Coefficient
		C = C * (i - j) // j
	print()