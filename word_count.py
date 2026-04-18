'''
Brya Cota
CSC101
2/25/26
This program will count the number of words within a given string. Word counting is a simple yet powerful
method in text preprocessing, crucial for tokenization, frequency analysis, and data cleaning.
'''

# Prompt the user to enter a sentence or paragraph of your choice.
words_to_count = input("Please enter a sentence or paragraph of your choice: ")

# Strip any leading and trailing whitespace from the input.
stripped_words = words_to_count.split()

# Replace multiple spaces with a single space.
replace_words = words_to_count.replace("  ", " ")

# Split the sentence into individual words.
split_words = words_to_count.split()

# Count the number of words and display the result.
counted_split_words = len(split_words)
print(f"Word count: {counted_split_words}")

# Display the first and last word from the sentence.
print(f"First word: {stripped_words[0]}")
print(f"Last word: {stripped_words[-1]}")

# Display the sentence in uppercase and lowercase formats.
print(f"Uppercase word: {words_to_count.upper()}")
print(f"Lowercase word: {words_to_count.lower()}")

# Display a formatted message summarizing the word count.
print(f"Your text contains {counted_split_words} words.")

