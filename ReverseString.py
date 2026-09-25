# Reverse a string without using [::-1] 

text = "Python"
reverse = ""

for ch in text:
    reverse = ch + reverse 
    
print(reverse)