import sys
read = sys.stdin.readline

direction = (1, -1, 0, 0)


def dfs(zone, row, col, team, count):
    for i in range(4):
        new_row = row + direction[i]
        new_col = col + direction[3-i]
        if 0 <= new_row < m and 0 <= new_col < n:
            if zone[new_row][new_col] == team:
                count += 1
                zone[new_row][new_col] = 2

                count = dfs(zone, new_row, new_col, team, count)
    return count


def calculate(zone, row_len, col_len):
    w_power, b_power = 0, 0
    count = 0
    for row_i in range(row_len):
        for col_i in range(col_len):
            if zone[row_i][col_i] == 0:
                zone[row_i][col_i] = 2
                count = 1
                w_num = dfs(zone, row_i, col_i, 0, count)
                w_power += w_num**2
            elif zone[row_i][col_i] == 1:
                zone[row_i][col_i] = 2
                count = 1
                b_num = dfs(zone, row_i, col_i, 1, count)
                b_power += b_num**2
    print(w_power, b_power)


war_zone = []
n, m = map(int, read().rstrip().split())
for i in range(m):
    war_zone.append([])
    str = read().rstrip()
    for j in range(n):
        if str[j] == 'W':
            war_zone[i].append(0)
        else:
            war_zone[i].append(1)

calculate(war_zone, m, n)
