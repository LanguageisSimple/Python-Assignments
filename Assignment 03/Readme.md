# Assignment 3

## Problem Statement

Write a Python Program in which the user will provide two inputs, and the program will use the Floor Division Assignment Operator (//=) to compute and display the result.

## Instructions

1. The program should prompt the user to enter two numbers.
2. The program should use the floor division assignment operator (//=) to divide the first number by the second number and assign the result to the first number.
3. Finally, the program should print the result of the operation.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Taking the input from the user and storing it in a variable named `a`:**
   ```python
   a = int(input("Enter the first number: "))
   ```
   This line of code prompts the user to enter the first number and stores it as an integer in the variable `a`.

2. **Taking the second input from the user and storing it in a variable named `b`:**
   ```python
   b = int(input("Enter the second number: "))
   ```
   This line of code prompts the user to enter the second number and stores it as an integer in the variable `b`.

3. **Using the floor division assignment operator (//=):**
   ```python
   a //= b
   ```
   This line divides `a` by `b`, performs floor division, and assigns the result back to `a`.

4. **Printing the result:**
   ```python
   print(a)
   ```
   This line prints the result of the floor division assignment operation.

## How to Run the Program

1. Save the code in a file named `Assignment 3.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python Assignment 3.py
   ```
5. Follow the on-screen prompts to enter two numbers.

## Example

```sh
$ python Assignment 3.py
Enter the first number: 15
Enter the second number: 4
3
```

In this example, the user entered `15` as the first number and `4` as the second number. The program performed floor division (15 // 4) and the result `3` was printed.
