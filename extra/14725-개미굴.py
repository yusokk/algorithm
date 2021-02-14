import sys
import heapq
read = sys.stdin.readline

# key 1 = 현재 floor
trie = {1: 0}


def insert(data):
    current = trie
    i = trie[1]
    for char in data:
        i += 1
        if char not in current:
            current[char] = {1: i}
        current = current[char]


def draw(data):
    current = trie
    for char in data:
        if 0 not in current[char]:
            current[char][0] = 1
            temp = "--" * current[1] + char
            print(temp)
        current = current[char]


n = int(read())
heap = []
for _ in range(n):
    temp = read().rstrip()
    feed_list = temp[2:].split()
    insert(feed_list)
    heapq.heappush(heap, feed_list)

for _ in range(n):
    feed = heapq.heappop(heap)
    draw(feed)