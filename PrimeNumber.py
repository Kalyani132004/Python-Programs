# Check whether a number is prime 

def check_prime(num):
    if num <= 1:
        return False 
    
    for i in range(2, num):
        if num % i == 0:
            return False 
        
    return True 

num = 19

if check_prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")