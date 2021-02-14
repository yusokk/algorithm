coordinates = input().split()
x = int(coordinates[0])
y = int(coordinates[1])
w = int(coordinates[2])
h = int(coordinates[3])

def min_path(a, b, c, d):
    horizontal = 0
    vertical = 0
    if b-a < a-0:
        horizontal = b-a
    else:
        horizontal = a-0
    if d-c < c-0:
        vertical = d-c
    else:
        vertical = c-0

    if horizontal > vertical:
        print(vertical)
    else:
        print(horizontal)

min_path(x, w, y, h)