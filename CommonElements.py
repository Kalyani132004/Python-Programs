# Write a Python program to find common elements between two lists. 

def find_common_elements(list1, list2):
    common = [] 
    
    for num in list1:
        if num in list2 and num not in common:
            common.append(num)
            
    return common 

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = find_common_elements(list1, list2)
print("Common Elements: ", result)