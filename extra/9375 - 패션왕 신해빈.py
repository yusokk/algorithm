def solution():
    cases = int(input())
    for case in range(cases):
        n = int(input())
        clothes_dict = {}
        for _ in range(n):
            clothes, category = input().rstrip().split()

            if not clothes_dict.get(category, 0):
                clothes_dict[category] = []
            clothes_dict[category].append(clothes)

        clothes_nums = list(map(len, clothes_dict.values()))

        if not clothes_nums:
            print(0)
            continue

        answer = 1
        for num in clothes_nums:
            answer *= num+1

        print(answer-1)

solution()