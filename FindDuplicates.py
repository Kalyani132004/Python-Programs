# Find Duplicate Elements in a List 

def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return duplicates

numbers = [1, 2, 3, 2, 4, 3, 5]

result = find_duplicates(numbers)

print("Duplicates Element: ", result)