
# Sequence pattern matching example - matches against value sequences

import math


# Set up some test data with different math operations
operations = [
    ["Add", 1, 2, 3, 4, 5],
    ["Mul", 5, 6],
    ["Add", 10, 20],
    ["Sqrt", 9],
]

result = 0

# TODO: process each operation along with the set of given numbers
for op in operations:
    match op:
        case "Add", num1,num2:
            result = num2 +num1
        case "Mul", num1,num2:
            result = num2 * num1
        case "Sqrt", num:
            result = math.sqrt(num)
        case _:
            continue

    print(f"{op}: {result}")
