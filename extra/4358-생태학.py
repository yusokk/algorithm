import sys
sys.stdin = open("../test/input.txt", "r")
read = sys.stdin.readline
heap = []
trie = {}
check = {}

def insert(data):
    current = trie
    for char in data:
        if char not in current:
            current[char] = {}
        current = current[char]
    if 1 not in current:
        current[1] = 1
    else:
        current[1] += 1


def percent(data):
    current = trie
    for char in data:
        current = current[char]
    n = current[1]/tree_len * 100
    print("%s %.4f" % (data, n))

tree_len = 0
while True:
    temp = read().rstrip()
    if temp == "":
        break
    insert(temp)
    tree_len += 1
    if temp not in check:
        check[temp] = 1
        heap.append(temp)


heap.sort(reverse=True)

while heap:
    tree = heap.pop()
    percent(tree)