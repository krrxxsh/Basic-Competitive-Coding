def arithmetic():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    sum = n1 + n2
    mul = n1 * n2
    sub = n1 - n2
    div = n1 / n2
    return sum, mul, sub, div

result = arithmetic()
print("Sum:", result[0])
print("Multiplication:", result[1])
print("Subtraction:", result[2])
print("Division:", result[3])