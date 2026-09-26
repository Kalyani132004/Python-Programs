# Check Whether Two Strings Are Anagrams 

def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True 
    else:
        return False 
    
str1 = "listen"
str2 = "silent"

if check_anagram(str1, str2):
    print("Anagram")
else:
    print("Not Anagram")