class Book():
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def checkout(self):
    if self.available == True:
      self.available = False
      return True
    elif self.available == False:
      return False

  def return_book(self):
    self.available = True

  def display_info(self):
    print(f"Title: {self.title}\n Author: {self.author}")
    print()

###############################################################################

class Library():
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def display_books(self):
    for book in self.books:
      book.display_info()

  def get_book_by_title(self, title):
    for book in self.books:
      if title == book.title:
        return book
      else:
        print("Book not in library")
        return

###############################################################################

book1 = Book("Lord of the Rings", "JRR Tolkien")
book2 = Book("Game of Thrones", "JR Martin")
book3 = Book("The Hobbit", "JRR Tolkien")
#books = [book1, book2, book3]
#for book in books:
#  book.display_info()


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()
