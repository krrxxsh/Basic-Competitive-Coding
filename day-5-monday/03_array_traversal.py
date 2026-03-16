mylist = [ 5, 2, 9, 1, 5, 6 ]

# Traversing the list using for loop
def SearchElement(target):
    for i in range(len(mylist)):
        if target == mylist[i]:
            return i
        return -1

Result = SearchElement(9)
if Result != -1:
    print("Element found at index:", Result)
else:
    print("Element not found in the list.")