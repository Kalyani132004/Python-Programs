# Write a Python program to sort a list without using the sort() function.

def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                
    return numbers 
    
numbers = [5, 2, 8, 1, 3]
result = sort_list(numbers)
print("Sorted List: ", result)