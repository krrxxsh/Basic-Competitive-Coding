a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

max_value = a
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
if d > max_value:
    max_value = d
if e > max_value:
    max_value = e

print(f"The maximum value is: {max_value}")