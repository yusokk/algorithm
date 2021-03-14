import sys
from collections import deque
read = sys.stdin.readline


def merge_sort(A, B):
    dq_a = deque(A)
    dq_b = deque(B)
    ans_list = []
    while True:
        if not dq_a or not dq_b:
            break
        if dq_a[0] > dq_b[0]:
            ans_list.append(dq_b.popleft())
        else:
            ans_list.append(dq_a.popleft())
    if dq_a:
        while dq_a:
            ans_list.append(dq_a.popleft())
    else:
        while dq_b:
            ans_list.append(dq_b.popleft())
    print(*ans_list)


noob = read()
A = list(map(int, read().rstrip().split()))
B = list(map(int, read().rstrip().split()))
merge_sort(A, B)