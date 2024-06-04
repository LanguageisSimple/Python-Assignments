# Assignment 6

## Problem Statement

Write a Python program to find the square root of a number using the `math` module.

## Instructions

1. The program should prompt the user to enter a number.
2. The program should use the `sqrt` function from the `math` module to find the square root of the entered number.
3. Finally, the program should print the square root of the number.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Importing the `math` module:**
   ```python
   import math
   ```
   This line imports the `math` module, which provides mathematical functions, including the `sqrt` function used to calculate the square root.

2. **Taking input from the user and storing it in a variable named `num`:**
   ```python
   num = int(input("Enter a number: "))
   ```
   This line of code prompts the user to enter a number and stores it as an integer in the variable `num`.

3. **Finding the square root of the user's entered number:**
   ```python
   sqr = math.sqrt(num)
   ```
   This line calculates the square root of `num` using the `sqrt` function from the `math` module and stores the result in the variable `sqr`.

4. **Printing the result:**
   ```python
   print(f"The square root of {num} is: {sqr}")
   ```
   This line prints the square root of the number in a formatted string.

## How to Run the Program

1. Save the code in a file named `Assignment 6.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 6.py"
   ```
5. Follow the on-screen prompt to enter a number.

## Example

```sh
$ python "Assignment 6.py"
Enter a number: 16
The square root of 16 is: 4.0
```

In this example, the user entered `16` as the input. The program calculated the square root of `16` and printed `4.0`.
