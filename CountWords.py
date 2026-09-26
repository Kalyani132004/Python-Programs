# Count the Number of Words in a String 

def count_words(text):
    words = text.split()
    
    return len(words)

text = "Python is easy to learn"
result = count_words(text)

print("Number of words:", result)