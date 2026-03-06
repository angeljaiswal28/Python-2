class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def checkout_book(self):
        if self.available:
            self.available = False
            print(self.book_name, "has been issued.")
        else:
            print(self.book_name, "is currently not available.")

    def return_book(self):
        self.available = True
        print(self.book_name, "has been returned.")

    def display_book(self):
        status = "Available" if self.available else "Not Available"
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Status:", status)


# Main Program
book1 = Library("Python Programming", "Guido van Rossum")

book1.display_book()
book1.checkout_book()
book1.display_book()
book1.return_book()
book1.display_book()v
