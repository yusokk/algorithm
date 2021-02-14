import sys
read = sys.stdin.readline

trie = {}


def insert(data):
    current_node = trie
    for char in data:
        if char not in current_node:
            current_node[char] = {}
        current_node = current_node[char]
    current_node[1] = 1


def search(data):
    current_node = trie
    for char in data:
        if char not in current_node:
            return False
        current_node = current_node[char]
    if 1 in current_node:
        return True
    else:
        return False


n, m = map(int, read().rstrip().split())
for _ in range(n):
    data = read().rstrip()
    insert(data)

answer = 0
for _ in range(m):
    data = read().rstrip()
    if search(data):
        answer += 1

print(answer)
