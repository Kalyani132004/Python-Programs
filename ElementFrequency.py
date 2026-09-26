# Count Frequency of Each Element in a List 

def count_frequency(numbers):
    frequency = {}
    
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
            
        else:
            
            frequency[num] = 1 
    return frequency 

numbers = [1, 2, 2, 3, 3, 3, 4]
result = count_frequency(numbers) 

print("Frequency: ", result)