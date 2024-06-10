def char_to_ascii(alphabet):
    # This function takes a single character as input and returns its ASCII value.
    if len(alphabet) == 1:
        # If the input is a single character, convert it to ASCII using the built-in ord function.
        return ord(alphabet)
    else:
        # If the input is not a single character, print an error message.
        print("Input must be a single character.")

input_char = input("Enter a character: ")
# Get a character input from the user.

ascii_value = char_to_ascii(input_char)
# Call the char_to_ascii function with the user's input and store the result.

print(f"The ASCII value of '{input_char}' is: {ascii_value}")
# Print the ASCII value of the input character to the console.