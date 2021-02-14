import sys
sys.stdin = open("../test/1.txt", "r")
read = sys.stdin.readline

N = int(read())
registered = []
meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, read().rstrip().split())))

meetings.sort()
for meeting in meetings:
    start, end = meeting
    if not registered or registered[-1][1] <= start:
        registered.append((start, end))
    elif registered[-1][1] > end:
        registered.pop()
        registered.append((start, end))

print(len(registered))