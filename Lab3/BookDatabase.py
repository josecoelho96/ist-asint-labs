from book import Book
import pickle


class BookDatabase:

    book_id = 0

    def __init__(self):
        try:
            with open('bookdatabase.bk', 'rb') as f:
                try:
                    self.books = pickle.load(f)
                    BookDatabase.book_id = len(self.books)
                except EOFError:
                    self.books = list()
        except FileNotFoundError:
            self.books = list()

    def addBook(self, author, title, pub_date):
        book = Book(author, title, pub_date, BookDatabase.book_id)
        BookDatabase.book_id += 1
        self.books.append(book)
        with open('bookdatabase.bk', 'wb') as f:
            pickle.dump(self.books, f)

    def searchBook(self, identifier):
        for book in self.books:
            if book.identifier == identifier:
                return book

    def listBooks(self, author):
        author_books = list()
        for book in self.books:
            if book.author == author:
                author_books.append(book)
        return author_books
