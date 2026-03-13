name = "Krrish"
newname = ""
for i in name:
    if i not in newname:
        newname = newname + i
print("Original string:", name)
print("String after removing duplicates:", newname)

