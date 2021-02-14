import sys
sys.stdin = open("../test/most-close-two-point.txt", "r")
sys.setrecursionlimit(10**6)
num = int(input())
points = list()
for _ in range(num):
    points.append(list(map(int, sys.stdin.readline().split())))

points.sort()
min_square = (8*10)**8

def find(left, right):
    center = (left + right) // 2
    d = min(min_square, find(left, center))
    d = min(min_square, find(center, right))