n = int(input())
costs = list(list(map(int, input().split())) for _ in range(n))

check = 1 << n
min_cost = 10000000


def tsp(city, cost):
    global min_cost, check
    if min_cost <= cost:
        return
    if check + 1 == 1 << n+1:
        min_cost = min(min_cost, cost + costs[city][start])
        return

    for next_city in range(n):
        if next_city == city or check & (1 << next_city) == 1 << next_city or costs[city][next_city] == 0:
            continue
        check |= 1 << next_city
        tsp(next_city, cost + costs[city][next_city])
        check -= 1 << next_city


for start in range(n):
    check |= 1 << start
    tsp(start, 0)
    check -= 1 << start

print(min_cost)