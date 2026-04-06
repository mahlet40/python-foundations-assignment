# Function to count a, e, i, o, u in a sentence
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Testing the function
sentence = "Python is amazing"
print(f"Number of vowels in '{sentence}': {count_vowels(sentence)}")