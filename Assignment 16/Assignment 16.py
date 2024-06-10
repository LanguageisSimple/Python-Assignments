def reverse_string_original(string_input):
    # This function takes a string as input and returns the reversed string using slicing.
    return string_input[::-1]
    # Use Python's slicing feature to extract the characters in reverse order.

def reverse_string_iteration(string_input):
    # This function takes a string as input and returns the reversed string using iteration.
    reversed_string = ""
    # Initialize an empty string to store the reversed characters.
    for char in string_input:
        # Iterate over each character in the input string.
        reversed_string = char + reversed_string
        # Prepend each character to the reversed string.
    return reversed_string

input_string = input("Enter a sentence: ")
# Get a sentence input from the user.

reversed_slicing = reverse_string_original(input_string)
# Call the reverse_string_original function with the input string and store the result.

print(f"Reversed (Slicing): {reversed_slicing}")
# Print the reversed string using slicing to the console.

reversed_iteration = reverse_string_iteration(input_string)
# Call the reverse_string_iteration function with the input string and store the result.

print(f"Reversed (Iteration): {reversed_iteration}")
# Print the reversed string using iteration to the console.