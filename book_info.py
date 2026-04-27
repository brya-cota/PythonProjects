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
