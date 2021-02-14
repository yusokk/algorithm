import sys
sys.stdin = open("../test/color-paper.txt", "r")
length = int(sys.stdin.readline())
square = list()
for _ in range(length):
    temp_list = list(map(int, sys.stdin.readline().split()))
    square.append(temp_list)
b_count = 0
w_count = 0

def cut_color(cut_list, n):
    half = n//2
    global w_count, b_count

    if n == 1:
        if 0 in cut_list[0]:                # 한칸일 때 흰색이면 w+1
            w_count += 1
            return
        else:                               # 아니면 b+1
            b_count += 1
            return
    is_white = False
    is_blue = False

    for i in range(len(cut_list)):          # 각 줄마다 흰,파 있는지 확인
        if 0 in cut_list[i]:
            is_white = True
        if 1 in cut_list[i]:
            is_blue = True

    if is_white and is_blue:                # 있다면 1, 2, 3, 4 사분면 새로 리스트에 담아주고 재귀
        list_1 = list()
        list_2 = list()
        list_3 = list()
        list_4 = list()
        for i in range(half):
            list_1.append(cut_list[i][:half])
        for i in range(half):
            list_2.append(cut_list[i][half:])
        for i in range(half):
            list_3.append(cut_list[i+half][:half])
        for i in range(half):
            list_4.append(cut_list[i+half][half:])
        cut_color(list_1, half)
        cut_color(list_2, half)
        cut_color(list_3, half)
        cut_color(list_4, half)
    elif is_white:                               # 흰색만 있을 때
        w_count += 1
        return
    else:                                        # 파랑만 있을 때
        b_count += 1
        return

cut_color(square, length)

print(w_count)
print(b_count)