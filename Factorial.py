# Find factorial of a number. 

def factorial(num):
    result = 1 
    
    for i in range(1, num + 1):
        result = result * i
        
    return result 

num = 5
print("Factorial: ", factorial(num))