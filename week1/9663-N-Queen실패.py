N = int(input())
record_list = list(None for i in range(N))

count = 0
row = 0

def set(n, row):
    global count
    for i in range(n):
        col = i
        if col not in record_list:
            for index, item in enumerate(record_list):
                if item != None:
                    if abs(row-index) == abs(col-item):
                        break
            else:
                record_list[row] = col
                if row < n - 1:
                    set(n, row + 1)
                    record_list[row] = None
                else:
                    count += 1
                    record_list[row] = None

def n_queen(n, row):
    global count
    if n == 1:
        count += 1
    else:
        for i  in range(n):
            record_list[row] = i
            set(n, row +1)
            record_list[row] = None

n_queen(N, row)

print(count)