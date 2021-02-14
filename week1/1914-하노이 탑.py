test_num = int(input())
tower_list = [[], [], []]
tower_now = None
tower_next = None

def hanoi_count(n):
    if n > 1:
        return hanoi_count(n-1) * 2 + 1
    else:
        return 1
ans = hanoi_count(test_num)

def hanoi(n):
    for i in range(1, test_num+1):
        tower_list[0].append(i)
    hanoi_move_2(n)

def hanoi_move_2(n):
    if n > 1:
        hanoi_move_1(n-1)
        move_2(n)
        hanoi_move_1(n-1)
    else:
        move_2(1)

def hanoi_move_1(n):
    if n > 1:
        hanoi_move_2(n-1)
        move_1(n)
        hanoi_move_2(n-1)
    else:
        move_1(1)



def move_2(n):
    for i in range(3):
        if n in tower_list[i]:
            tower_now = i
            tower_next = (i + 2) % 3
            # print(f'{tower_now + 1} {tower_next + 1}')
            print("before ", tower_list)
            pop_disc = tower_list[tower_now].pop(0)
            if tower_list[tower_next]:
                if tower_list[tower_next][0] < pop_disc:
                    tower_list[tower_next].append(pop_disc)
                else:
                    tower_list[tower_next].insert(0, pop_disc)
            else:
                tower_list[tower_next].append(pop_disc)
            print("after ", tower_list)
            break

def move_1(n):
    for i in range(3):
        if n in tower_list[i]:
            tower_now = i
            tower_next = (i + 1) % 3
            print("before ", tower_list)
            pop_disc = tower_list[tower_now].pop(0)
            if tower_list[tower_next]:
                if tower_list[tower_next][0] < pop_disc:
                    tower_list[tower_next].append(pop_disc)
                else:
                    tower_list[tower_next].insert(0, pop_disc)
            else:
                tower_list[tower_next].append(pop_disc)
            print("after ", tower_list)
            break
if test_num <= 20:
    hanoi(test_num)