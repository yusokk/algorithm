n, m = map(int, input().split())

if n >= 3:
    if 4 <= m < 7:
        print(4)
    elif m <= 3:
        print(m)
    else:
        print(m-2)
elif n == 2:
    print((m+1)//2 if m <= 8 else 4)
else:
    print(1)