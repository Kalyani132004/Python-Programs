# Write a Python program to find the missing number from a list. 

def find_missing_number(numbers):
    n = len(numbers) + 1 
    
    total = n * (n + 1) // 2     
    corrent_sum = 0 
    for num in numbers:
        corrent_sum += num 
        
    return total - corrent_sum 

numbers = [1, 2, 3, 5, 6]

result = find_missing_number(numbers)
print("Missing Numbers: ", result)
