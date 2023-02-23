def factorial(n):
    for i in range(0,n):
        fact_n = n * (n-i)
        return fact_n
    
print(factorial(3))