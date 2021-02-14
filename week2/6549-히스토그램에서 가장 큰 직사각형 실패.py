# 히스토그램 스택버전 import sys
input = sys.stdin.readline
# sys.stdin = open("/Users/jewerlykim/Desktop/week1/백준 문제 파일/week02/baekjoon/txt/9.txt", 'r')
def solve():
    stack = []
    max_size = 0
    for i in range(len(rects)):
        start_point = i
        while stack and stack[-1][0] > rects[i]:
            height, start_point = stack.pop()
            max_size = max(max_size, height*(i-start_point))
        stack.append([rects[i], start_point])
    for height, start_point in stack:
        max_size = max(max_size, height*(len(rects)-start_point))
    return max_size
while True:
    N, *rects = map(int, input().split())
    if N != 0:
        print(solve())
    else:
        break


# 히스토그램에서 가장 큰 직사각형 ( 분할정복)
# 직사각형의 개수 vs 높이 높이가 가장 높은 놈 vs 1
# 딱 그 높이이상으로 잘렸을 때 만 인덱스 1 연속된 인덱스의 렝쓰가
import sys
#sys.stdin = open("/Users/jewerlykim/Desktop/week1/백준 문제 파일/week02/baekjoon/txt/9.txt", 'r')
input=sys.stdin.readline
def get_max(left, right):
    mid = (left + right) // 2
    if left == right :
        return height[left]
    # 접점을 포함하는 사각형의 최대 넓이 계산
    # mid와 mid+1 두개만 포함하는 경우
    tempHeight = min(height[mid:mid+2])
    tempAria = 2 * tempHeight
    # 그외의 길이의 경우
    ll, rr = mid, mid + 1
    # ll과 rr이 모두 범위 밖에 나가면 종료
    while left < ll or rr < right:
        # ll과 rr이 가리키는 높이를 비교해서, 큰쪽으로 커진다.
        # print(ll, rr)
        if rr < right and (ll == left or height[ll-1] < height[rr+1]):
            rr+=1
            tempHeight = min(tempHeight, height[rr])
        else:
            ll-=1
            tempHeight = min(tempHeight, height[ll])
        tempAria = max(tempAria, tempHeight * (rr-ll+1))
    # 왼쪽 분할 오른쪽 분할, 그리고 접접을 포함하는 area 중에서 제일 큰 값을 리턴
    return max(get_max(left,mid), get_max(mid+1, right), tempAria)
while True:
    height = list(map(int,input().split()))
    answer = -1
    if height[0] == 0: # 0이면 프로그램 종료
        break
    N = height[0]
    print(get_max(1,N))