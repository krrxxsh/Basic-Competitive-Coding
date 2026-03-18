arr = [0, 1, 0, 3, 12]

for value in arr[:]:
    if value == 0:
        arr.remove(value)
        arr.append(value)

print(arr)
