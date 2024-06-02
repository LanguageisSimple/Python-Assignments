# Assignment 5

## Problem Statement

Write a Python program in which the user will provide one input, and this input will be stored in one variable and then assigned to another variable using the equal sign (=).

## Instructions

1. The program should prompt the user to enter a number.
2. The program should store the input in one variable and then assign the value of this variable to another variable using the equal sign (=).
3. Finally, the program should print the value of the second variable.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Taking input from the user and storing it in a variable named `a`:**
   ```python
   a = int(input("Enter the first number: "))
   ```
   This line of code prompts the user to enter a number and stores it as an integer in the variable `a`.

2. **Assigning the value of `a` to another variable named `b`:**
   ```python
   b = a
   ```
   This line assigns the value stored in `a` to the variable `b`.

3. **Printing the result:**
   ```python
   print(b)
   ```
   This line prints the value of the variable `b`.

## How to Run the Program

1. Save the code in a file named `Assignment 5.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 5.py"
   ```
5. Follow the on-screen prompts to enter a number.

## Example

```sh
$ python "Assignment 5.py"
Enter the first number: 42
42
```

In this example, the user entered `42` as the input. The program stored the value in variable `a`, assigned it to variable `b`, and printed `b`, resulting in `42`.
