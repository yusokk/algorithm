import sys
sys.stdin = open("../test/max_diff.txt")
import itertools
test_num = int(input())
test_list = list(map(int, input().split()))

sorted_list = list(itertools.permutations(test_list, test_num))
len_list = list()
pre_val = None
ans_list = list()
for tuple in sorted_list:
    for index in range(len(tuple)):
        if index > 0:
            len_list.append(tuple[index]-pre_val)
            pre_val = tuple[index]
        else:
            pre_val = tuple[index]
    abs_len_list = list(map(abs, len_list))
    len_list = []
    list_sum = sum(abs_len_list)
    ans_list.append(list_sum)
ans = max(ans_list)
print(ans)