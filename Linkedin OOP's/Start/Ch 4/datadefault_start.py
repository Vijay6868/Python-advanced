# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,50))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No Author"
    pages: int = 0
    #price: float = field(default = 10.0)
    price: float = field(default_factory=price_func)

b1 = Book()
print(b1)

b2 = Book("Harry potter", "JK rawling",200)
b3 = Book("Harry potter", "JK rawling",200)
print(b2)
print(b3)


