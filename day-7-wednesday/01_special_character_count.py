var = "gasgg54@#vscd!s*"
count = 0

for ch in var:
    code = ord(ch)
    if 97 <= code <= 122:
        continue
    elif 48 <= code <= 57:
        continue
    else:
        count += 1

print(count)
