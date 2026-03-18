# dict = {'c': 97, 'a':98, 'b':98}
# for _ in sorted(dict):
#     print(dict[_])

fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1 
addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))
