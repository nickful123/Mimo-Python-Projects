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



book1 = Book("Lord of the Rings", "JRR Tolkien")
book2 = Book("Game of Thrones", "JR Martin")
book3 = Book("The Hobbit", "JRR Tolkien")
books = [book1, book2, book3]


for book in books:
  book.display_info()
