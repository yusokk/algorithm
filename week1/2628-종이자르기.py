full_len = list(int(i) for i in input().split())
full_width = [1, full_len[0]]
full_height = [0, full_len[1]]

width_list = list([full_width])
height_list = list([full_height])

test_num = int(input())
for n in range(test_num):
    temp_list = list(map(int, input().split()))
    if temp_list[0] == 1:
        width_list.append(temp_list)
    else:
        height_list.append(temp_list)
def sort_func(e):
    return e[1]
width_list.sort(key = sort_func)
height_list.sort(key = sort_func)

def find_max(list):
    max_num = 0
    previous = 0
    for index in range(len(list)):
        if list[index][1] - previous > max_num:
            max_num = list[index][1] - previous
        previous = list[index][1]
    return max_num

max_width = find_max(width_list)
max_height = find_max(height_list)

ans = max_width * max_height
print(ans)