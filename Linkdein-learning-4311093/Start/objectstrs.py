# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Vijay"
        self.lname = "Kumar"
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person Class - fname:{self.fname}, lname:{self.lname}, age:{self.age}>"
    # TODO: use str for a more human-readable string
    def __str__(self):
        
        return f"Person {self.fname} {self.lname} {self.age}"
    
    def __bytes__(self):
        val = f"Person {self.fname} {self.lname} {self.age}"
        return bytes(val.encode("utf-8"))


# create a new Person object
cls1 = Person()

# use different Python functions to convert it to a string
print(repr(cls1))
print(str(cls1))
print(f"Formatted: {cls1}")
print(cls1.__bytes__())