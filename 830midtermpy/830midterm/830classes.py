import csv
import pandas as pd

sortingbooks = pd.read_csv("BookSheet.csv")

class BookLibrarian(object):
    def books(self):
        sortingbooks = pd.read_csv("BookSheet.csv")
        return sortingbooks

class ReturnList(object):

    def Author_List(self):
        booklist = BookLibrarian()
        books = booklist.books()
        authors =  books
        author_books = authors.sort_values(['Author'], ascending=[True])
        print(author_books)

    def Title_List(self):
        booklist = BookLibrarian()
        books = booklist.books()
        titles = books
        titles_books = titles.sort_values(['Title'], ascending=[True])
        print(titles_books)

    def Year_Published(self):
        booklist = BookLibrarian()
        books = booklist.books()
        yearpub = books
        year_pub = yearpub.sort_values(['YearPublished'], ascending=[True])
        print(year_pub)

    def Book_Summary(self):
        booklist = BookLibrarian()
        books = booklist.books()
        booksum =  books
        book_summary = booksum.sort_values(['Summary'], ascending=[True])
        print(book_summary)
