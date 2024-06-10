from collections import Counter
import string

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

file_path = './Assets/sample_text.txt'  
# Specify the file path for which we want to count word occurrences.

word_occurrences = count_word_occurrences(file_path)
# Call the count_word_occurrences function with the file path and store the result.

if word_occurrences:
    # Check if the word occurrences were successfully counted.
    print("Word occurrences:")
    for word, count in word_occurrences.items():
        # Iterate over the word counts and print each word with its count.
        print(f"{word}: {count}")
else:
    print("Word occurrences could not be determined.")
    # Print a message if the word occurrences could not be determined.