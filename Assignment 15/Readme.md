# Assignment 15

## Problem Statement

Create a function that takes a list as input and returns the count of a specific element within that list.

## Instructions

1. The program should prompt the user to enter a list of elements.
2. The program should then ask for a target element whose occurrences need to be counted in the list.
3. The program should use a function to count the occurrences of the target element in the list.
4. Finally, the program should print the count of the target element.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Define the `count_element_in_list` function:**
   ```python
   def count_element_in_list(input_list, target_element):
       # This function takes a list and a target element as input, and returns the count of the target element in the list.
       return input_list.count(target_element)
       # Use the built-in count method of the list to count the occurrences of the target element.
   ```
   This function takes a list and a target element as input and returns the count of the target element using the built-in `count` method of the list.

2. **Prompt the user to enter the elements of the list:**
   ```python
   print("Enter the elements of the List (space-separated): ")
   ```
   This line prints a message prompting the user to enter the elements of the list.

3. **Read and process the user input:**
   ```python
   my_list = list(map(int, input().split()))
   ```
   This line reads the input from the user, splits it into individual elements, converts them to integers, and stores them in a list.

4. **Prompt the user to enter the target element:**
   ```python
   target_element = int(input("Enter the target number: "))
   ```
   This line reads the target element from the user and converts it to an integer.

5. **Call the `count_element_in_list` function and store the result:**
   ```python
   element_count = count_element_in_list(my_list, target_element)
   ```
   This line calls the `count_element_in_list` function with the list and target element, and stores the result in the `element_count` variable.

6. **Print the result:**
   ```python
   print(f"The count of {target_element} in the list is: {element_count}")
   ```
   This line prints the count of the target element in the list to the console.

## How to Run the Program

1. Save the code in a file named `Assignment 15.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using the following command:
   ```sh
   python "Assignment 15.py"
   ```

## Example

When prompted, enter the elements of the list followed by the target number:
```sh
$ python "Assignment 15.py"
Enter the elements of the List (space-separated): 
1 2 3 4 5 1 1 2
Enter the target number: 1
The count of 1 in the list is: 3
```

In this example, the program reads the list of elements and the target number from the user, counts the occurrences of the target number in the list, and prints the result.
