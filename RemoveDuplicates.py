# Remove duplicate elements from a list.

def remove_duplicates(numbers):
    unique = []
    
    for num in numbers:
        if num not in unique:
            unique.append(num)
            
    return unique

numbers = [1, 2, 2, 3, 4, 4, 5]

result = remove_duplicates(numbers)

print("List after removing duplicates: ", result)