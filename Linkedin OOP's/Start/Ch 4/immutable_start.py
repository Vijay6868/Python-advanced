# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def setValue1(self, value):
        self.value1 = "harry"
obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
#obj.value1 = "harry"

# TODO: even functions within the class can't change anything
#obj.setValue1("harry")