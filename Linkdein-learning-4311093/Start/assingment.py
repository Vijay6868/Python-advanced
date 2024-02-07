
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

# TODO: the assignment operator is part of an expression
#x:=10)
#print(x)

# TODO: The assignment expression is useful for writing concise code

thestr = input("value?")
while thestr != "exit":
    print(thestr)
    thestr = input("value?")


# TODO: The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": len(values),
    "total": sum(values),
    "average": sum(values) / len(values)
}

y = 7
print(y)

val = [10,40,50,90]
x = len(val)
valData = {
    "lenght": (l:=len(val)),
    "total":  (s:=sum(val)),
    "average":s/l
}
print.pp(valData)
