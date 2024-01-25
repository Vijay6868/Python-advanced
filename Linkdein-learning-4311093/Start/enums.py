# define enumerations using the Enum base class
from enum import Enum, unique,auto

# TODO: enums have human-readable values and types
class Fruit(Enum):
    KIWI = auto()
    APPLE = 1
    BANANA = 2
    ORANGE =1
    TOMATO =4


# TODO: enums have name and value properties
print(Fruit.APPLE.value)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))

# TODO: print the auto-generated value
print(Fruit.KIWI.value)
# TODO: enums are hashable - can be used as keys
my_fruits = {
 
}
my_fruits[Fruit.BANANA]="come mr husky"
print(my_fruits[Fruit.BANANA])
