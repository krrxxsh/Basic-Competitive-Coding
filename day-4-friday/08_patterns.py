# # for i in range(1, 4):
# #     for j in range(1, 4):
# #         print(i, end = " ")
# #     print()

# for i in range(1, 4):
#     for j in range(4, 1, -1):
#         print(i, end = " ")
#     print()

n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(n+1-i, end = " ")
    print()