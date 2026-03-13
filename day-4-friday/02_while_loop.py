# i = 1
# while i<=5:
#     print(i)
#     i = i+1

# username = ''
# password = ''

# while username != "admin" and password != "hello":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

n = int(input("Enter a number: "))
sum = 0
i = 1
while i<=n:
    sum = sum + i
    i = i+1
print("Sum of first", n, "natural numbers is:", sum)