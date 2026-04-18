'''
Brya Cota
2/25/26
This program helps us learn about basic data structures: lists, tuples, dictionaries, and sets
'''
# Create a list of five favorite books. Add a new book to the list and display the updated list.
favorite_books = ["Pretty Girls", "Saving Noah", "Sharp Objects", "Gone Girl", "Dark Places"]
favorite_books.append("The Housemaid")
print(favorite_books)

# Create a tuple with three student details (name, major, graduation year). Display each item using indexing.
student = ("Brya", "AI/ML", "2028")
print(student[0])
print(student[1])
print(student[2])

# Create a dictionary with three key-value pairs representing a book (book title, author, cost).
# Add another key-value pair and print the updated dictionary.
book = {
    "Book Title" : "Gone Girl",
    "Cost" : "$10.99",
    "Author" : "Gillian Flynn"
}

book["Critics Rating "] = "4.2/5"
print(book)

# Create a set of four unique zip codes. Add a new zipcode to the set and print the final set.
zip_codes = {85225, 85286, 85282, 85296}
zip_codes.add(85295)
print(zip_codes)

# The difference between lists and tuples are that tuples are immutable - meaning they cannot be changed after creation. These are typically used when working with data that shouldn't be modified.
# You can access elements in a tuples and lists by indexing. Although, the index methods differ between the two.
# Since a set can only have unique elements, when adding a duplicate value to a set, it is ignored.
