def factorial_recursive(n):
    # This function calculates the factorial of a given number using recursion.
    if n == 0 or n == 1:
        # Base case: if n is 0 or 1, the factorial is 1.
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial_recursive(n - 1)

number = int(input("Enter the number whose factorial you want to find: "))
# Get the number from the user for which we want to calculate the factorial.

factorial_result = factorial_recursive(number)
# Call the factorial_recursive function with the number and store the result.

print(f"The factorial of {number} is: {factorial_result}")
# Print the factorial result to the console.