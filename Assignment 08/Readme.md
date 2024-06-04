# Assignment 8

## Problem Statement

Write a Python program to take two inputs from the user and use the Multiplication Assignment Operator (*=) to give the result.

## Instructions

1. The program should prompt the user to enter two numbers.
2. The program should multiply the first number by the second number using the multiplication assignment operator (*=) and assign the result to the first number.
3. Finally, the program should print the result of the operation.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Taking input from the user and storing it in a variable named `a`:**
   ```python
   a = int(input("Enter the first number: "))
   ```
   This line of code prompts the user to enter the first number and stores it as an integer in the variable `a`.

2. **Taking the second input from the user and storing it in a variable named `b`:**
   ```python
   b = int(input("Enter the second number: "))
   ```
   This line of code prompts the user to enter the second number and stores it as an integer in the variable `b`.

3. **Multiplying `a` by `b` and storing the result in `a` using the multiplication assignment operator (*=):**
   ```python
   a *= b
   ```
   This line multiplies `a` by `b` and assigns the result back to `a`.

4. **Printing the result:**
   ```python
   print(a)
   ```
   This line prints the result of the multiplication operation.

## How to Run the Program

1. Save the code in a file named `Assignment 8.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 8.py"
   ```
5. Follow the on-screen prompts to enter two numbers.

## Example

```sh
$ python "Assignment 8.py"
Enter the first number: 6
Enter the second number: 7
42
```

In this example, the user entered `6` as the first number and `7` as the second number. The program multiplied `6` by `7` using the multiplication assignment operator and printed `42`.
