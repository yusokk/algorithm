num = int(input())

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.que = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.no = 0

    def enque(self, val):
        self.que[self.rear] = val
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        if self.no > 1:
            self.front += 1
            if self.front == self.capacity:
                self.front = 0
            self.que[self.rear] = self.que[self.front]
            self.front += 1
            self.rear += 1
            self.no -= 1
            if self.rear == self.capacity:
                self.rear = 0
        else:
            print(self.que[self.front])


card_q = Queue(5000000)
for i in range(1, num+1):
    card_q.enque(i)

while card_q.no > 1:
    card_q.deque()
card_q.deque()