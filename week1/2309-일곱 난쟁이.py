height_list = list()
for i in range(9):
    height = int(input())
    height_list.append(height)

height_list.sort()

difference = sum(height_list) - 100

def find(height_list):
    for i in range(9):
        for j in range(9):
            if 8-i > j:
                if height_list[8-i] + height_list[j] > difference:
                    break
                elif height_list[8-i] + height_list[j] == difference:
                    del1 = height_list[8-i]
                    del2 = height_list[j]
                    height_list.remove(del1)
                    height_list.remove(del2)
                    return height_list
            else:
                break
height_list = find(height_list)
for i in height_list:
    print(i)