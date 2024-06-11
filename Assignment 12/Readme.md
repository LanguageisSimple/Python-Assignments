# Assignment 12

## Problem Statement

Write a function that takes a character (alphabet) as input and returns its corresponding ASCII value.

## Instructions

1. The program should prompt the user to enter a single character.
2. The program should use a function to convert the character to its corresponding ASCII value.
3. Finally, the program should print the ASCII value of the input character.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Define the `char_to_ascii` function:**
   ```python
   def char_to_ascii(alphabet):
       # This function takes a single character as input and returns its ASCII value.
       if len(alphabet) == 1:
           # If the input is a single character, convert it to ASCII using the built-in ord function.
           return ord(alphabet)
       else:
           # If the input is not a single character, print an error message.
           print("Input must be a single character.")
   ```
   This function checks if the input is a single character and then returns its ASCII value using the `ord` function. If the input is not a single character, it prints an error message.

2. **Get a character input from the user:**
   ```python
   input_char = input("Enter a character: ")
   ```
   This line of code prompts the user to enter a character and stores it in the variable `input_char`.

3. **Call the `char_to_ascii` function with the user's input and store the result:**
   ```python
   ascii_value = char_to_ascii(input_char)
   ```
   This line calls the `char_to_ascii` function with the user's input and stores the returned ASCII value in the variable `ascii_value`.

4. **Print the ASCII value of the input character:**
   ```python
   print(f"The ASCII value of '{input_char}' is: {ascii_value}")
   ```
   This line prints the ASCII value of the input character to the console.

## How to Run the Program

1. Save the code in a file named `Assignment 12.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 12.py"
   ```
5. Follow the on-screen prompt to enter a character.

## Example

```sh
$ python "Assignment 12.py"
Enter a character: A
The ASCII value of 'A' is: 65
```

In this example, the user entered the character `A`. The program converted the character to its ASCII value, which is `65`, and printed the result.
