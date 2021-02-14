import sys
read = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.child = {}
        self.data = data

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, data):
        cur_node = self.head
        for char in data:
            if cur_node.data:
                return False
            if char not in cur_node.child:
                cur_node.child[char] = Node(None)
            cur_node = cur_node.child[char]
        if cur_node.child:
            return False
        cur_node.data = data
        return True


t = int(read())
for _ in range(t):
    n = int(read())
    flag = False
    phone_trie = Trie()
    for _ in range(n):
        if flag:
            read()
            continue
        if not phone_trie.insert(read().rstrip()):
            print("NO")
            flag = True
    else:
        if not flag:
            print("YES")
