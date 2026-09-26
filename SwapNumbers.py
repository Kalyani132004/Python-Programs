# Swap Two Numbers Without Using a Third Variable 

def swap_variable(a, b):
    a, b = b, a 
    
    return a, b 

a = 10 
b = 20 

print("Before Swapping: ")
print("a =", a)
print("b =", b)

a, b = swap_variable(a, b)

print("After Swapping: ")
print("a =", a)
print("b =", b)