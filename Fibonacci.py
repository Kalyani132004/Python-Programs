# Write a Python program to generate the Fibonacci series. 

def fibonacci(n):
    a = 0 
    b = 1 
    
    for i in range(n):
        print(a, end=" ")
        
        c = a + b 
        a = b 
        b = c 
        
n = 8 
fibonacci(n)