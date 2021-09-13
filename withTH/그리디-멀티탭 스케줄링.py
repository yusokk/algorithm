import heapq
n, k = map(int, input().split())
plugs = input().split()

order_dict = {}

# 순서 팝하기 좋게 반대로?
for i in range(k-1, -1, -1):
    if not order_dict.get(plugs[i], 0):
        order_dict[plugs[i]] = []
    order_dict[plugs[i]].append(k-i)

count = 0
current_uses = []

for plug in plugs:
    order_dict[plug].pop()
    for used_plug in current_uses:
        if used_plug[1] == plug:
            current_uses.remove(used_plug)
            heapq.heappush(current_uses, [order_dict[plug][-1] if order_dict[plug] else 0, plug])
            break
    else:
        if len(current_uses) < n:
            heapq.heappush(current_uses, [order_dict[plug][-1] if order_dict[plug] else 0, plug])
        else:
            heapq.heappop(current_uses)
            heapq.heappush(current_uses, [order_dict[plug][-1] if order_dict[plug] else 0, plug])
            count += 1

print(count)

