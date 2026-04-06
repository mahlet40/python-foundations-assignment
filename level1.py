# Function to reverse any text provided
def reverse_string(text):
    return text[::-1]

# Testing the function
user_input = "Hello World"
print(f"Original: {user_input}")
print(f"Reversed: {reverse_string(user_input)}")