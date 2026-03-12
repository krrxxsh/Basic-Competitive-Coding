mydict = {
    101: "Prashant",
    102: "Ashish",
    103: "Komal",
    104: "Ankush",
    "106": "Sandip",
    "107": 60.52,
    "108": True
}
print(mydict)

mydict[109] = "Harsh"
print(mydict)

for x,y in mydict.items():
    print(x,y)