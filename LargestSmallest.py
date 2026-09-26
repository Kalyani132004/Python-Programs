# Find the largest and smallest number in a list.

def find_largest_smallest(numbers):
    largest = numbers[0]
    smallest =numbers[0]
    
    for num in numbers:
        if  num > largest:
            largest = num 
            
        if num < smallest:
            smallest = num 
            
    return largest, smallest 

numbers = [10, 5, 25, 8, 2]

largest, smallest = find_largest_smallest(numbers)

print("Largest: ", largest)
print("Smallest: ", smallest)