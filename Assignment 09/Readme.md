# Assignment 9

## Problem Statement

Write a Python program to take two inputs from the user and use the Addition Assignment Operator (+=) to give the result.

## Instructions

1. The program should prompt the user to enter two numbers.
2. The program should add the second number to the first number using the addition assignment operator (+=) and assign the result to the first number.
3. Finally, the program should print the result of the operation.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Taking input from the user and storing it in a variable named `a`:**
   ```python
   a = int(input("Enter the 1st number: "))
   ```
   This line of code prompts the user to enter the first number and stores it as an integer in the variable `a`.

2. **Taking the second input from the user and storing it in a variable named `b`:**
   ```python
   b = int(input("Enter the 2nd number: "))
   ```
   This line of code prompts the user to enter the second number and stores it as an integer in the variable `b`.

3. **Adding `b` to `a` and storing the result in `a` using the addition assignment operator (+=):**
   ```python
   a += b
   ```
   This line adds `b` to `a` and assigns the result back to `a`.

4. **Printing the result:**
   ```python
   print(a)
   ```
   This line prints the result of the addition operation.

## How to Run the Program

1. Save the code in a file named `Assignment 9.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 9.py"
   ```
5. Follow the on-screen prompts to enter two numbers.

## Example

```sh
$ python "Assignment 9.py"
Enter the 1st number: 5
Enter the 2nd number: 7
12
```

In this example, the user entered `5` as the first number and `7` as the second number. The program added `7` to `5` using the addition assignment operator and printed `12`.
