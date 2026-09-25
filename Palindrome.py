# Check whether a string is a palindrome 

def check_palindrome(text):
    reverse = "" 
    
    for ch in text:
        reverse = ch + reverse 
        
    if text == reverse:
        return True 
    else: 
        return False 
    
text = "madam"

if check_palindrome(text):
    print("Palindrome") 
else:
    print("Not Palindrome")