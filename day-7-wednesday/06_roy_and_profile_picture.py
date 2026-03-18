# HackerEarth: Roy and Profile Picture
input_data = """180
3
640 480
120 300
180 180"""

input_list = input_data.split("\n")
input = lambda: input_list.pop(0)

L = int(input())
N = int(input())

for _ in range(N):
    W, H = map(int, input().split())

    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")
