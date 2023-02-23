# write a program factorial of a number using functions
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:

    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)

#write a program to calculate simple interestdef simple_interest(p,t,r):

def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
     
     
# Driver code
P = int(input("Enter the principle amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simple_interest(P,T,R)



