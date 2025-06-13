"""
1) creating library system that keeps track of books, borrower, availability, allowing borrowing, returning, availability check.
2) include due dates, penalty for the late returns and the uniuque id for the books and the users.

"""


class Library:
    def __init__(self):
        self.books = {}

    def add_books(self, id, title, author, total_copies):
        book = Books(id, title, author, total_copies)
        self.books[id] = book
        print(f"Book {title} added to the library!")


    def check_availability(self, book_id):
        if book_id in self.books:
            book = self.books(book_id)
            if book.available_copies > 0:
                print(f"Book {book.title} is available!")
            else:
                print(f"Book {book.title} is not avialable!")

    def borrow(self, user_id, book_id):
        pass

    def return_book(self, user_id,  book_id):
        pass




class Books:
    def __init__(self, id, title, author, total_copies, borrowed_by) :
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.borrowed_by = borrowed_by 

        
        


   





class User:
    pass
