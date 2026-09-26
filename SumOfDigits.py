# Write a Python program to find the sum of digits of a number. 

def sum_of_digits(num):
    total = 0 
    
    while num > 0:
        digit = num % 10 
        total = total + digit 
        num = num // 10 
        
    return total 

num = 1234
result = sum_of_digits(num)
print("Sum of Digits: ", result)