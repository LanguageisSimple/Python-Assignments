# Assignment 14

## Problem Statement

Write a Python script to read a text file and count the occurrences of each word.

## Instructions

1. The program should read the content of a specified text file.
2. The program should count the occurrences of each word in the file, ignoring case differences.
3. The program should handle punctuation appropriately.
4. Finally, the program should print the word counts.

## Solution

The provided Python program accomplishes the task with the following steps:

1. **Import necessary modules:**
   ```python
   from collections import Counter
   import string
   ```
   These imports provide the necessary tools for counting word occurrences and handling punctuation.

2. **Define the `count_word_occurrences` function:**
   ```python
   def count_word_occurrences(file_path):
       # This function reads a file, counts the occurrences of each word, and returns a dictionary with the word counts.
       try:
           with open(file_path, 'r', encoding='utf-8') as file:
               # Open the file in read mode with UTF-8 encoding to handle special characters.
               content = file.read().lower()
               # Read the file content and convert it to lowercase to ignore case differences.
               translator = str.maketrans('', '', string.punctuation)
               # Create a translator to remove punctuation from the content.
               words = content.translate(translator).split()
               # Remove punctuation and split the content into individual words.
               word_counts = Counter(words)
               # Count the occurrences of each word using the Counter class.
               return word_counts
       except FileNotFoundError:
           # Handle the exception when the file is not found.
           print(f"File not found: {file_path}")
           return None
   ```
   This function reads a file, converts its content to lowercase, removes punctuation, splits the content into words, and counts the occurrences of each word using the `Counter` class from the `collections` module. If the file is not found, it prints an error message.

3. **Specify the file path:**
   ```python
   file_path = './Assets/sample_text.txt'
   ```
   This line specifies the file path of the text file to be read.

4. **Call the `count_word_occurrences` function and store the result:**
   ```python
   word_occurrences = count_word_occurrences(file_path)
   ```
   This line calls the `count_word_occurrences` function with the specified file path and stores the result in the `word_occurrences` variable.

5. **Print the word occurrences:**
   ```python
   if word_occurrences:
       # Check if the word occurrences were successfully counted.
       print("Word occurrences:")
       for word, count in word_occurrences.items():
           # Iterate over the word counts and print each word with its count.
           print(f"{word}: {count}")
   else:
       print("Word occurrences could not be determined.")
       # Print a message if the word occurrences could not be determined.
   ```
   This block checks if word occurrences were successfully counted and prints each word with its count. If the counting was unsuccessful, it prints an error message.

## How to Run the Program

1. Save the code in a file named `Assignment 14.py`.
2. Ensure you have a text file located at `./Assets/sample_text.txt` with some sample text.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is saved.
5. Run the program using the following command:
   ```sh
   python "Assignment 14.py"
   ```

## Example

Assuming `sample_text.txt` contains the following text:
```
Hello world!
Hello Python world.
```

The output will be:
```sh
$ python "Assignment 14.py"
Word occurrences:
hello: 2
world: 2
python: 1
```

In this example, the program reads the file, counts the occurrences of each word (ignoring case and punctuation), and prints the result.
