# Check Armstrong Number 

def check_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0 
    
    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10 
        
    return total == original 

num = 153 

if check_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
 