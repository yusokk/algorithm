import sys
sys.stdin = open("../test/yosepus.txt", "r")
N_K = list(map(int, input().split()))

N = N_K[0]
K = N_K[1]

class YoseQueue:
    def __init__(self, cap):
        self.cap = cap
        self.frt = 0
        self.rear = 0
        self.no = 0
        self.que = [None] * self.cap

    def enque(self, val):
        self.que[self.rear] = val
        self.rear += 1
        self.no += 1
        if self.rear == self.cap:
            self.rear = 0

    def deque(self, n):
        for _ in range(n-1):
            self.que[self.rear] = self.que[self.frt]
            self.rear += 1
            self.frt += 1
            if self.rear == self.cap:
                self.rear = 0
            if self.frt == self.cap:
                self.frt = 0
        x = self.que[self.frt]
        self.frt += 1
        self.no -= 1
        if self.frt == self.cap:
            self.frt = 0
        return x

    def is_empty(self):
        return self.no > 0


yo_que = YoseQueue(2000)
out_list = list()

for i in range(1, N+1):
    yo_que.enque(i)

while yo_que.is_empty():
    out = yo_que.deque(K)
    out_list.append(out)
print_string = "<"
i = 0

while i < len(out_list)-1:
    print_string = print_string + str(out_list[i]) + ", "
    i += 1
ans = print_string + str(out_list[len(out_list)-1]) + ">"
print(ans)