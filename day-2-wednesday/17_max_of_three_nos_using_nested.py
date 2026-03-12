a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b:
    if a>c:
        print(f"The maximum value is: {a}")
    else:
        print(f"The maximum value is: {c}")

else:
    if b>c:
        print(f"The maximum value is: {b}")
    else:
        print(f"The maximum value is: {c}")

