arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
arr3 = [3, 4, 5]

common = set(arr1) & set(arr2) & set(arr3)
result = list(common)

print(result)
