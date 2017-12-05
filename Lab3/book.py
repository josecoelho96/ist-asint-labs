class Book:

    def __init__(self, author, title, pub_date, identifier):
        self.author = author
        self.title = title
        self.pub_date = pub_date
        self.identifier = identifier

    def printBookInfo(self):
        print("Author: " + str(self.author))
        print("Title: " + str(self.title))
        print("Publication Date: " + str(self.pub_date))
        print("Identifier: " + str(self.identifier))

