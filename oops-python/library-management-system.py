"""
1) creating library system that keeps track of books, borrower, availability, allowing borrowing, returning, availability check.
2) include due dates, penalty for the late returns and the uniuque id for the books and the users.

"""

from datetime import datetime, timedelta
import random
class Book:
    def __init__(self, bid, title, author, total_copies):
        self.bid = bid
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.borrow_by ={}

    # def check_availability(self, bid):
    #     book = self.books[bid]
    #     if book.available_copies >0:
    #         print(f"{book.title} is available. Available copies are: {book.available_copies}")
    #     else:
    #         print("Book not Found!")

    def is_available(self):
        return self.available_copies > 0
    
    def borrow(self,user_id ):
        if self.is_available():
            due_date = datetime.now() + timedelta(days=7)
            self.available_copies -= 1
            self.borrow_by[user_id] = due_date
            print(f"{self.title} has borrowed by user - {user_id} due till {due_date.date()}")
        else:
            print(f"{self.title} is not available!")
    
    def return_book(self, user_id):
        if user_id in self.borrow_by:
            due_date = self.borrow_by[user_id]
            self.available_copies += 1
            del self.borrow_by[user_id]
            today = datetime.now()
            if today > due_date:
                late_days = (today - due_date).day
                fine = late_days *5
                print(f"User {user_id} has late return fine of ${fine} for {late_days} days late!")
            else:
                print("Book return successfull!")
        else:
            print("You did't borrow any books!")

class User:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(1000, 9999)
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.user = {}
        self.books = {}

    def add_book(self, title, author, total_copies):
        bid = random.randint(1000, 9999)
        self.books[bid] = Book(bid, title, author, total_copies)
        print(f"The book {title} has been added with id {bid}")
    
    def register_user(self, name):
        user = User(name)
        self.user[user.id] = user
        print(f"User {name} has been registered to the Library with id {user.id}")
        return user.id

    def borrow_book(self, book_id, user_id):
        if user_id in self.user and book_id in self.books:
            self.books[book_id].borrow(user_id)
            self.user[user_id].borrowed_books.append(book_id)
        else:
            print("Invalid user or book!")
    
    def return_books(self, book_id, user_id):
        if user_id in self.user and book_id in self.books:
            self.books[book_id].return_book(user_id)
            if book_id in self.user[user_id].borrowed_books: 
                self.user[user_id].borrowed_books.remove(book_id)
        else:
            print("Invalid user or book!")

    def check_availability(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            print(f"The book {book.title} is available! Available copies {book.available_copies}")
        else:
            print("Book not found!")

    def all_books(self):
        if self.books:
            for book in self.books.values():
                print(f"{book.title} - {book.author} - {book.total_copies}")
        else:
            print("No books Available")

    def all_users(self):
        if self.user:
            for user in self.user.values():
                print(f"{user.name} - {user.id}")
        else:
            print("No user availabel!")
            

library = Library()

while True:
    print("\n1. Add book\n2. Register User\n3. Borrow Book\n4. Return Book\n5. Check Availability\n6. All books\n7. All users\n8. Exit\n")
    choice = int(input(">> "))

    if choice == 1:
        title = input("Enter title of book: ")
        author = input("Enter the author of book: ")
        copies = int(input("Enter the total copies: "))
        library.add_book(title, author, copies)

    elif choice == 2:
        name = input("Enter your name: ")
        library.register_user(name)

    elif choice == 3:
        user_id = int(input("Enter users id: "))
        book_id = int(input("Enter books id: "))
        library.borrow_book(book_id, user_id)
    elif choice == 4:
        user_id = int(input("Enter user id: "))
        book_id = int(input("Enter book id: "))
        library.return_books(book_id, user_id)

    elif choice == 5:
        book_id = int(input("Enter book id: "))
        library.check_availability(book_id)

    elif choice == 6:
        library.all_books()

    elif choice == 7:
        library.all_users()

    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid Input!")

