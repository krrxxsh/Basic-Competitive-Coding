physics = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))
mathematics = int(input("Enter mathematics marks: "))

total_marks = physics + chemistry + mathematics
percentage = (total_marks / 300) * 100

if percentage >= 60:
    print("Eligible for palcement")
else:
    print("Not eligible for placement")
