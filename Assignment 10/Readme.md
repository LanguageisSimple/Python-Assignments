# Assignment 10

## Problem Statement

Write a Python program to take two inputs from the user and use the Modulus Assignment Operator (%=) to give the result.

## Instructions

1. The program should prompt the user to enter two numbers.
2. The program should calculate the modulus of the first number by the second number using the modulus assignment operator (%=) and assign the result to the first number.
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

3. **Calculating the modulus of `a` by `b` and storing the result in `a` using the modulus assignment operator (%=):**
   ```python
   a %= b
   ```
   This line calculates the modulus of `a` by `b` and assigns the result back to `a`.

4. **Printing the result:**
   ```python
   print(a)
   ```
   This line prints the result of the modulus operation.

## How to Run the Program

1. Save the code in a file named `Assignment 10.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 10.py"
   ```
5. Follow the on-screen prompts to enter two numbers.

## Example

```sh
$ python "Assignment 10.py"
Enter the first number: 10
Enter the second number: 3
1
```

In this example, the user entered `10` as the first number and `3` as the second number. The program calculated the modulus of `10` by `3` (10 % 3) and printed `1`.
