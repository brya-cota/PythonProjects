'''
Brya Cota
2/23/26
This program will show you how to manipulate strings using built-in string function, underatnd how
to format strings for output.
'''

# Prompting the user for their name, favorite quote, and favorite word from that quote. input() function already
# returns a string as default.
full_name = input("Please enter your full name: ")
quote = input("Please enter your favorite quote: ")
word = input("Please enter your favorite word from your favorite quote: ")

# Print the length of the full name.
print (len(full_name))

# Convert the full name to uppercase and lowercase.
uppercase_name = full_name.upper()
print(uppercase_name)

lowercase_name = full_name.lower()
print(lowercase_name)

# Print the title-cased (the first character of each word is uppercase) version of the favorite quote.
titlecase_quote = quote.title()
print(titlecase_quote)

# Replace spaces in the favorite quote with hyphens.
new_quote = quote.replace(" ", "-")
print(new_quote)

# Find the position of the first occurrence of the favorite word in the favorite quote.
index = quote.find(word)
print(index)

# Combine the full name and favorite quote into one formatted string.
name_quote = full_name + " " + quote
print(name_quote)

# Strip any leading or trailing whitespace from the quote or phrase.
strip_quote = quote.strip()
print(strip_quote)

# Uses f-strings for all output
print(f'You full name is: {full_name}. Your favorite quote is: {quote}. Your favoritr word from your favorite quote is: {word}.')








