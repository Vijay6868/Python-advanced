
# Demonstrate the use of lambda functions


# TODO: define a function that takes variable arguments
def addition(*args):
    result =0
    for arg in args:
        result+=arg
    return result


# TODO: pass different arguments
print(addition(10,11))

# TODO: pass an existing list
myNums = [10,20,40]

print(addition(*myNums)) # unpack List using * at front of list variable