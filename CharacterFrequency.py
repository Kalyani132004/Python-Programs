# Find Character Frequency in a String 

def character_frequency(text):
    frequency = {}
    
    for char in text:
        if char in frequency:
            frequency[char] += 1 
        else:
            frequency[char] = 1 
            
    return frequency 

text = "Python"

result = character_frequency(text)
print("Character Frequency:", result)