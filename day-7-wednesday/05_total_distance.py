arr = [10, 11, 7, 12, 14]
size = len(arr)


def total_distance(size, arr):
    distance = 0
    for i in range(size - 1):
        distance += abs(arr[i] - arr[i + 1])
    return distance


result = total_distance(size, arr)
print(result)
