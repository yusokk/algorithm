n, k = map(int, input().split())
cargo = [tuple(map(int, input().split())) for _ in range(n)]

dp = dict()
dp[0] = 0

for w, v in cargo:
    temp = []
    for dp_w, dp_v in dp.items():
        if dp_w + w <= k:
            temp.append((dp_w+w, dp_v+v))
    for temp_w, temp_v in temp:
        if dp.get(temp_w):
            if dp[temp_w] < temp_v:
                dp[temp_w] = temp_v
        else:
            dp[temp_w] = temp_v
print(max(dp.values()))