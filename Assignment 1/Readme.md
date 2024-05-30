# Assignment 1

## Problem Statement

Write a Python Program in which the user will provide input in a floating point data type, and the program will return the integer value of the floating point data type.

## Instructions

1. The program should prompt the user to enter a number in floating point format.
2. The program should then convert this floating point number to its integer equivalent.
3. Finally, the program should print the integer value.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Taking input from the user in floating point data type:**
   ```python
   a = float(input("Enter a number : "))
   ```
   This line of code prompts the user to enter a number and stores it as a float in the variable `a`.

2. **Storing the integer value of `a` in another variable named `b`:**
   ```python
   b = int(a)
   ```
   This line converts the floating point number `a` to an integer and stores it in the variable `b`.

3. **Printing the value of `b`, which is the integer value of `a`:**
   ```python
   print(b)
   ```
   This line prints the integer value stored in `b`.

## How to Run the Program

1. Save the code in a file named `assignment1.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python assignment1.py
   ```
5. Follow the on-screen prompt to enter a floating point number.

## Example

```sh
$ python assignment1.py
Enter a number : 3.14
3
```

In this example, the user entered `3.14`, and the program output `3`, which is the integer value of the floating point number.
