test_num = int(input())

def count(num):
    ans = 0
    cnt = 0
    if num < 100:
        ans = num
    elif 100 <= num < 1000:
        for n in range(100, num+1):
            test_list = str(n)
            a = int(test_list[0])
            b = int(test_list[1])
            c = int(test_list[2])
            if a-b == b-c:
                cnt += 1
        ans = cnt + 99
    else:
        ans = count(999)
    return ans

answer = count(test_num)
print(answer)