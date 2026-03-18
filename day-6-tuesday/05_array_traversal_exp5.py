array = [1, 2, 3, 4]
n = len(array)


new_array = [1] * n


left_product = 1
for i in range(n):
    new_array[i] = left_product
    left_product *= array[i]


right_product = 1
for i in range(n - 1, -1, -1):
    new_array[i] *= right_product
    right_product *= array[i]

print(new_array)