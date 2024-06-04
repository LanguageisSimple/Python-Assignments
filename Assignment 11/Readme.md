# Assignment 11

## Problem Statement

Write a Python program to take a word as input and print the number of vowels in the word.

## Instructions

1. The program should prompt the user to enter a word.
2. The program should count the number of vowels (a, e, i, o, u) in the entered word.
3. Finally, the program should print the number of vowels in the word.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Taking input from the user:**
   ```python
   string = input("Enter a string: ")
   ```
   This line of code prompts the user to enter a string and stores it in the variable `string`.

2. **Initializing a variable named `vowelcount` to keep track of the number of vowels:**
   ```python
   vowelcount = 0
   ```
   This variable will store the count of vowels in the entered string.

3. **Converting the entered string to lowercase:**
   ```python
   string = string.lower()
   ```
   This line of code converts the entered string to lowercase to simplify the vowel checking process.

4. **Iterating through each character in the string using a for loop:**
   ```python
   for char in string:
   ```
   This loop iterates through each character in the string.

5. **Checking if the character is a vowel:**
   ```python
   if char in 'aeiou':
   ```
   This line of code checks if the current character is a vowel.

6. **Incrementing the `vowelcount` variable if the character is a vowel:**
   ```python
   vowelcount += 1
   ```
   If the character is a vowel, the `vowelcount` variable is incremented by 1.

7. **Printing the result:**
   ```python
   print("Number of vowels in the string:", vowelcount)
   ```
   This line prints the total number of vowels found in the entered string.

## How to Run the Program

1. Save the code in a file named `Assignment 11.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 11.py"
   ```
5. Follow the on-screen prompt to enter a word.

## Example

```sh
$ python "Assignment 11.py"
Enter a string: Hello
Number of vowels in the string: 2
```

In this example, the user entered the word "Hello". The program counted the vowels (e and o) in the word and printed the result, which is `2`.
