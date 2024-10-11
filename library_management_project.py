class User:
    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.logged_in =False
    def login(self,eamil,password):
        if self.email == email and self.password == password:
            self.logged_in = True
            print(f"{self.email} logged out.")     
        else:
            print("login failed. incorrect email or password")   
    

    def logout(self):
        self.logged_in = False
        print(f"{self.email} logged out.")

class LibraryUser(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.borrowed_books = []

    def borrow_book(self, library, book_title):
        if not self.logged_in:
            print("Please log in first.")
            return
        book = library.get_book(book_title)
        if book and book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"Book '{book.title}' borrowed successfully.")
        else:
            print(f"Book '{book_title}' is not available for borrowing.")

    def return_book(self, library, book_title):
        if not self.logged_in:
            print("Please log in first.")
            return
        for book in self.borrowed_books:
            if book.title == book_title:
                book.available = True
                self.borrowed_books.remove(book)
                library.return_book(book)
                print(f"Book '{book.title}' returned successfully.")
                return
        print(f"You don't have '{book_title}' borrowed.")

    def check_available_books(self, library):
        if not self.logged_in:
            print("Please log in first.")
            return
        library.show_available_books()

class Admin(User):
    def __init__(self, email, password):
        super().__init__(email, password)

    def add_book(self, library, title, author):
        if not self.logged_in:
            print("Please log in first.")
            return
        new_book = Book(title, author)
        library.add_book(new_book)
        print(f"Book '{title}' added successfully.")

    def check_available_books(self, library):
        if not self.logged_in:
            print("Please log in first.")
            return
        library.show_available_books()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.admins = []

    def register_user(self, email, password):
        user = LibraryUser(email, password)
        self.users.append(user)
        print(f"User account for {email} created.")
        return user

    def register_admin(self, email, password):
        admin = Admin(email, password)
        self.admins.append(admin)
        print(f"Admin account for {email} created.")
        return admin

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def return_book(self, book):
        if book not in self.books:
            self.books.append(book)

    def show_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author} (Available)")
        else:
            print("No books available.")

# Example usage:

# Creating the library instance
library = Library()

# Registering a user
user = library.register_user("user1@example.com", "password123")

# Registering an admin
admin = library.register_admin("admin1@example.com", "adminpassword")

# Admin logs in and adds books
admin.login("admin1@example.com", "adminpassword")
admin.add_book(library, "The Great Gatsby", "F. Scott Fitzgerald")
admin.add_book(library, "To Kill a Mockingbird", "Harper Lee")
admin.logout()

# User logs in and checks available books
user.login("user1@example.com", "password123")
user.check_available_books(library)

# User borrows a book
user.borrow_book(library, "The Great Gatsby")

# User checks available books again
user.check_available_books(library)

# User returns the book
user.return_book(library, "The Great Gatsby")

# User logs out
user.logout()

# Admin logs in to check available books
admin.login("admin1@example.com", "adminpassword")
admin.check_available_books(library)
admin.logout()
