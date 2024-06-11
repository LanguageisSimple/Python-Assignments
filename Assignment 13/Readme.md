# Assignment 13

## Problem Statement

Write a function to compute the factorial of a given number using recursion.

## Instructions

1. The program should prompt the user to enter a number.
2. The program should use a recursive function to calculate the factorial of the entered number.
3. Finally, the program should print the factorial of the input number.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Define the `factorial_recursive` function:**
   ```python
   def factorial_recursive(n):
       # This function calculates the factorial of a given number using recursion.
       if n == 0 or n == 1:
           # Base case: if n is 0 or 1, the factorial is 1.
           return 1
       else:
           # Recursive case: n! = n * (n-1)!
           return n * factorial_recursive(n - 1)
   ```
   This function uses recursion to calculate the factorial of a number. If the input number `n` is 0 or 1, the function returns 1 (base case). Otherwise, it returns `n` multiplied by the factorial of `n-1` (recursive case).

2. **Get the number from the user for which we want to calculate the factorial:**
   ```python
   number = int(input("Enter the number whose factorial you want to find: "))
   ```
   This line of code prompts the user to enter a number and stores it as an integer in the variable `number`.

3. **Call the `factorial_recursive` function with the number and store the result:**
   ```python
   factorial_result = factorial_recursive(number)
   ```
   This line calls the `factorial_recursive` function with the user's input number and stores the returned factorial value in the variable `factorial_result`.

4. **Print the factorial result to the console:**
   ```python
   print(f"The factorial of {number} is: {factorial_result}")
   ```
   This line prints the factorial of the input number to the console.

## How to Run the Program

1. Save the code in a file named `Assignment 13.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 13.py"
   ```
5. Follow the on-screen prompt to enter a number.

## Example

```sh
$ python "Assignment 13.py"
Enter the number whose factorial you want to find: 5
The factorial of 5 is: 120
```

In this example, the user entered `5`. The program calculated the factorial of `5` using the recursive function and printed `120`.
