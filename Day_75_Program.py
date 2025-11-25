"""
Create a class Book with attributes: title, author, and price.
Write a method display() to print book details.
Accept data for 3 books from the user, create objects, and write their details to a file called "books.txt"
"""
class Book:
    def __init__(self, t, a, p):
        self.title = t
        self.author = a
        self.price = p

    def display(self):
        return f"Title is {self.title}, Author is {self.author} and Price is {self.price}"


for _ in range(3):
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    price = input("Enter Book Price: ")
    b = Book(title, author, price)
    book_details = b.display()
    with open("books.txt", "a") as fp:
        fp.write(book_details + '\n')
