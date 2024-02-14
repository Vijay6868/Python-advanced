# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author =author
        self.pages =pages
        self.price = price

    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price-(self.price*self._discount)
        else:
            return self.price
    
    def setDiscount(self, amount):
        self._discount = amount

# TODO: create instances of the class
book2 = Book("Brave New World","Leo Tolstoy",1225,39.95)
book1 = Book("War and Peace","JD Salinger",234,29.95)
# TODO: print the class and property
print(book1)
print(book1.title)

print(book1.getPrice())
book1.setDiscount(0.25)
print(book1.getPrice())