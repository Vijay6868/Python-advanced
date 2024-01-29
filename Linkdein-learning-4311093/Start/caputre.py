# Capture pattern matching for assigning values within the match

name = input("What is your name? ")

match name:
    case "":
        print("Hello, anonymous!")
    case "Vijay" | "Enzo" as s:
        print(f"Hello {s}")
    case name:
        print(f"oh hello, {name}!")