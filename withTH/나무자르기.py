n, m = map(int, input().split())
trees = list(map(int, input().split()))


def binary_search():
    start = 0
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2
        current_sum = 0

        for tree in trees:
            if tree > mid:
                current_sum += tree-mid

        if current_sum > m:
            start = mid + 1
        else:
            end = mid - 1

    return start


print(binary_search())