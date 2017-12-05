from book import Book
from BookDatabase import BookDatabase

def main():

    # create a new book database
    database = BookDatabase()
    valid_operations = ["NEW", "SHOW", "LIST"]

    operation = input("Insert a operation to do: ")

    if operation not in valid_operations:
        print("ERROR: Wrong operation! Valid operations are: " + str(valid_operations))
        raise SystemExit

    if operation == "NEW":
        print("Insert the book information below")
        author = input("Author: ")
        title = input("Book title: ")
        pub_date = input("Publication date: ")
        database.addBook(author, title, pub_date)

    elif operation == "SHOW":
        identifier = input("Insert the book identifier: ")
        book = database.searchBook(identifier)
        if book:
            book.printBookInfo()
        else:
            print("No book was found!")

    elif operation == "LIST":
        author = input("Insert the book author: ")
        books = database.listBooks(author)
        for book in books:
            book.printBookInfo()


if __name__ == "__main__":
    main()