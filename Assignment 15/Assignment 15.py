def count_element_in_list(input_list, target_element):
    # This function takes a list and a target element as input, and returns the count of the target element in the list.
    return input_list.count(target_element)
    # Use the built-in count method of the list to count the occurrences of the target element.

print("Enter the elements of the List (space-separated): ")
# Prompt the user to enter the elements of the list.

my_list = list(map(int, input().split()))
# Read the input from the user, split it into individual elements, convert them to integers, and store them in a list.

target_element = int(input("Enter the target number: "))
# Read the target element from the user and convert it to an integer.

element_count = count_element_in_list(my_list, target_element)
# Call the count_element_in_list function with the list and target element, and store the result.

print(f"The count of {target_element} in the list is: {element_count}")
# Print the count of the target element in the list to the console.