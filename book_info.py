class Book:
    # Define the __init__() method to initialize the attributes
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

        pass

    # Implement the display_info() method to print the book’s title, author and price
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Original price: {self.price}")

        pass

    # Implement apply_discount() method to update the price based on a given discount.
    def apply_discount(self, discount):
        self.price = self.price * (1 - (discount/100))
        print("Discounted price: {:.2f}".format(self.price))

        pass

# Creating an instance of a Book object (outside of the class)
book1 = Book("1984", "Georgle Orwell", 19.99)

# Displaying the info of the book based on display_info() method
book1.display_info()

# Applying a 10% discount on the book based on the calculation in the apply_discount() method
book1.apply_discount(10)

# REVIEW QUESTIONS:
'''What does the self keyword refer to in your class methods?
The self keyword refers to the current instance of the class. It's used to access attributes and methods within the class
definition. 

What is the purpose of the __init__() method in the Book class?
The __init__ method is a special method used to initialize instance attributes. It acts as the constructor because it
constructs the objects. This specific method in the Book class initialized the attributes (variables) title, author, and 
price so we could use it in the ither class methods (only if you attach them to self). 

Which method would you call to reduce the price of a book?
apply_discount()

What will happen if you create a Book object with only one argument: book = Book("The Hobbit")?
A TypeError will be thrown because the other 2 required arguments are missing. 
'''