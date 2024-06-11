# Assignment 16

## Problem Statement

Create a function that reverses a string input using different methods (e.g., slicing, iteration).

## Instructions

1. The program should prompt the user to enter a sentence.
2. The program should provide two different functions to reverse the string:
    - Using slicing
    - Using iteration
3. The program should print the reversed string for both methods.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Define the `reverse_string_original` function:**
   ```python
   def reverse_string_original(string_input):
       # This function takes a string as input and returns the reversed string using slicing.
       return string_input[::-1]
       # Use Python's slicing feature to extract the characters in reverse order.
   ```
   This function takes a string as input and returns the reversed string using slicing.

2. **Define the `reverse_string_iteration` function:**
   ```python
   def reverse_string_iteration(string_input):
       # This function takes a string as input and returns the reversed string using iteration.
       reversed_string = ""
       # Initialize an empty string to store the reversed characters.
       for char in string_input:
           # Iterate over each character in the input string.
           reversed_string = char + reversed_string
           # Prepend each character to the reversed string.
       return reversed_string
   ```
   This function takes a string as input and returns the reversed string using iteration by prepending each character to a new string.

3. **Prompt the user to enter a sentence:**
   ```python
   input_string = input("Enter a sentence: ")
   ```
   This line gets a sentence input from the user.

4. **Reverse the string using slicing and print the result:**
   ```python
   reversed_slicing = reverse_string_original(input_string)
   print(f"Reversed (Slicing): {reversed_slicing}")
   ```
   These lines call the `reverse_string_original` function with the input string and print the reversed string using slicing.

5. **Reverse the string using iteration and print the result:**
   ```python
   reversed_iteration = reverse_string_iteration(input_string)
   print(f"Reversed (Iteration): {reversed_iteration}")
   ```
   These lines call the `reverse_string_iteration` function with the input string and print the reversed string using iteration.

## How to Run the Program

1. Save the code in a file named `Assignment 16.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 16.py"
   ```

## Example

When prompted, enter a sentence to see the reversed versions:
```sh
$ python "Assignment 16.py"
Enter a sentence: Hello World
Reversed (Slicing): dlroW olleH
Reversed (Iteration): dlroW olleH
```

In this example, the program reads a sentence from the user, reverses it using both slicing and iteration methods, and prints the reversed strings.
