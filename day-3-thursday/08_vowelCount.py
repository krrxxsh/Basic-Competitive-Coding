x = ['A', 'B', 'C']
y = ['A', 'B', 'C']
z = [1,2,3,4]

print(x==y)
print(x==z)
print(x!=z)

name = "Krish"
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0
consonentCount = 0
for n in name:
    if n in vowels:
        vowelCount += 1
    else:
        consonentCount += 1

print(f"Vowel Count: {vowelCount}")
print(f"Consonent Count: {consonentCount}")
