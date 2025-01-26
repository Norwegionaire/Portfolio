def add(x, y):
    return x + y

def multiply(x, y):
    return x*y

def addThenMultiply(x, y, z):
    return multiply(add(x, y), z)

a = int(input("Gib Numbah:"))
b = int(input("Gib Numbah:"))
c = int(input("Gib Numbah:"))
sum = addThenMultiply(a, b, c)

print("Sum of x, y and z is:", sum)
