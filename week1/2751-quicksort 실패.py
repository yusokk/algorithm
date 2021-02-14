import sys
sys.setrecursionlimit(10**8)
sys.stdin = open("../test/sort2.txt")

test_num = int(input())
test_list = list()
for i in range(test_num):
    num = int(input())
    test_list.append(num)

def sort3(list, a, b, c):
    if list[a] > list[b]: list[a], list[b] = list[b], list[a]
    if list[b] > list[c]: list[b], list[c] = list[c], list[b]
    if list[a] > list[b]: list[a], list[b] = list[b], list[a]
    return b

def qsort(list, left, right):
    pl = left
    pr = right
    med = list[(pl+pr) // 2]
    while pl < pr:
        while list[pl] < med: pl += 1
        while list[pr] > med: pr -= 1
        if pl <= pr:
            list[pl], list[pr] = list[pr], list[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(list, left, pr)
    if pl < right: qsort(list, pl, right)

def quick_sort(list, left, right):
    pl = left
    pr = right
    m = sort3(list, pl, (pl+pr)//2, pr)
    list[pr-1], list[m] = list[m], list[pr-1]
    pivot = list[pr-1]
    pl += 1
    pr -= 2
    while pl < pr:
        while list[pl] < pivot: pl += 1
        while list[pr] > pivot: pr -= 1
        if pl <= pr:
            list[pl], list[pr] = list[pr], list[pl]
            pl += 1
            pr -= 1
    if left < pr: qsort(list, left, pr)
    if pl < right: qsort(list, pl, right)

quick_sort(test_list, 0, len(test_list)-1)
for i in test_list:
    print(i)
