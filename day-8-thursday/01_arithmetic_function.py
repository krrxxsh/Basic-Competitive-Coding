def addition(num1, num2):
    return num1 + num2

def substraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "infinity"



while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your Choice: "))

    if choice == 5:
        break
    val1 = int(input("Enter the first Value: "))
    val2 = int(input("Enter the second Value: "))
    if choice == 1:
        print("Addition: ", addition(val1, val2))
    elif choice == 2:
        print("Substraction: ", substraction(val1, val2))
    elif choice == 3:
        print("Multiplication: ", multiplication(val1, val2))
    elif choice == 4:
        print("Division: ", division(val1, val2))
  
