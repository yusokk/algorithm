import sys
# sys.stdin = open("../test/cut-tree.txt", "r")
first_input = list(map(int, sys.stdin.readline().split()))
M = first_input[1]
trees = list(map(int, sys.stdin.readline().split()))
max_tree = max(trees)  # 나무 최대 높이 지정

def cut_tree(left, right):
    while True:
        med = (left + right) // 2
        tempM = 0
        preM = 0
        for tree in trees:
            if tree < med:
                m = 0
                pre_m = 0
            else:
                m = tree - med  # 나무들에서 중간값으로 잘라서 확인
                pre_m = tree - (med+1)
            tempM += m
            preM += pre_m
        if tempM == M:  # 같으면 나옴
            break
        elif tempM < M:  # 원하는 값보다 작으면 더 잘라야하니까 높이를 더 낮춤
            right = med - 1
        else:  # 아니면 반대로 높이를 높임
            if preM < M:
                break
            else:
                left = med + 1
    return med


ans = cut_tree(0, max_tree)
print(ans)