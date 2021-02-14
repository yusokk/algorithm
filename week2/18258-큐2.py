import sys
sys.stdin = open("../test/queue2.txt", "r")
n = int(sys.stdin.readline())
c_list = []
for _ in range(n):
    temp = sys.stdin.readline()
    c_list.append(temp)

class Queue:
    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * self.capacity

    def enque(self, val):
        self.que[self.rear] = val
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        if self.no > 0:
            x = self.que[self.front]
            self.front += 1
            self.no -= 1
            if self.front == self.capacity:
                self.front = 0
            print(x)
        else:
            print(-1)

    def __len__(self):
            return self.no

    def is_empty(self):
        if self.no <= 0:
            print(1)
        else:
            print(0)

    def forward(self):
        if self.no > 0:
            print(self.que[self.front])
        else:
            print(-1)

    def back(self):
        if self.no > 0:
            print(self.que[self.rear-1])
        else:
            print(-1)

queue = Queue(2000000)

def q_command(string):
    if string[:4] == "push":
        strings = string.split()
        queue.enque(int(strings[1]))
    elif string[:3] == "pop":
        queue.deque()
    elif string[:4] == "size":
        l = len(queue)
        print(l)
    elif string[:5] == "empty":
        queue.is_empty()
    elif string[:5] == "front":
        queue.forward()
    else:
        queue.back()

for c in c_list:
    q_command(c)