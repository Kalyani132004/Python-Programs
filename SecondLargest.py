# Find the Second-Largest Number in a List 

def find_second_largest(numbers):
    largest = numbers[0]
    second_largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            second_largest = largest 
            largest = num 
            
        elif num > second_largest and num != largest:
            second_largest = num 
            
    return second_largest 

numbers = [10, 25, 5, 40, 30]

result = find_second_largest(numbers)

print("Second Largest: ", result)
            