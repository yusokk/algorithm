test_num = int(input())
for index in range(test_num):
    input_list = list(int(i) for i in input().split())
    length = input_list[0]
    scores = input_list[1:]
    avg = sum(scores) / length
    count = 0
    for i in scores:
        if i > avg:
            count += 1
    rate = count / length * 100
    print(f"{rate:.3f}%")