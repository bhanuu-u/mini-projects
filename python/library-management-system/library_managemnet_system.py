import json


class Book:

    def __init__(self, bookname, author, available=True):
        self.bookname = bookname
        self.author = author
        self.available = available

    def display(self):
        print("=" * 20)
        print(f"Bookname : {self.bookname}")
        print(f"Author : {self.author}")
        print(f"Available : {self.available}")
        print("=" * 20)

    def borrow(self):
        if self.available == True:
            self.available = False
            print(f"The Book {self.bookname} has been borrowed successfully")
        elif self.available == False:
            print(f"The book {self.bookname} is not available")

    def return_book(self):
        if self.available == False:
            self.available = True
            print(f"The book {self.bookname} has been returned successfully")
        elif self.available == True:
            print(f"The book {self.bookname} is already at the library")


class library:

    def __init__(self):
        self.books = []

    def display_books(self):
        for book in self.books:
            book.display()

    def borrow_book(self, bookname):
        for book in self.books:
            if book.bookname == bookname:
                book.borrow()
                self.save_books()
                return

        print("Book not found")

    def return_book(self, bookname):
        for book in self.books:
            if book.bookname == bookname:
                book.return_book()
                self.save_books()
                return

        print("Book not found")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

        print("Book has been added successfully")

    def remove_book(self, bookname):
        for book in self.books:
            if book.bookname == bookname:
                self.books.remove(book)
                self.save_books()
                print("The book has been removed successfully")
                return

        print("There is no such book")

    def load_books(self):
        with open("books.json", "r") as file:
            data = json.load(file)

        for item in data:
            book = Book(
                item["bookname"],
                item["author"],
                item["available"]
            )

            self.books.append(book)

    def save_books(self):
        data = []

        for book in self.books:
            data.append({
                "bookname": book.bookname,
                "author": book.author,
                "available": book.available
            })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    def search_book(self,bookname):
        for book in self.books:
            if book.bookname == bookname:
                book.display()
                return

        print("Book Not Found")    


# # Create library object
# my_library = library()

# # # Load existing books from JSON
# my_library.load_books()

# # # Add a new book
# # book3 = Book("The Truth", "James gun")
# # my_library.add_book(book3)

# # # Display all books
# # my_library.display_books()

# # Borrow a book
# # my_library.borrow_book("1984")

# # Return a book
# # my_library.return_book("1984")

# # Remove a book
# # my_library.remove_book("1984")

# # Search book
# my_library.search_book("1984")