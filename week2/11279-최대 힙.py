import sys
sys.stdin = open("../test/max-heap.txt", 'r')
num = int(sys.stdin.readline())


class HeapQueue:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def push(self, val):
        if len(self.heap) == 0:
            self.heap.append(val)
        else:
            self.heap.append(val)
            self.temp = self.heap[len(self.heap)-1]  # 현재 값
            self.current = len(self.heap)-1          # 현재 위치
            while self.temp > self.heap[(self.current-1) // 2]:     # 현재 값이 부모 값보다 크면
                self.heap[self.current] = self.heap[(self.current-1) // 2]  # 현재 위치에 부모 값 줌
                self.current = (self.current-1) // 2
                if self.current == 0:
                    break
            self.heap[self.current] = self.temp

    def pop(self):
        if len(self.heap) > 0:
            x = self.heap[0]
            self.current = 0
            self.temp = self.heap[len(self.heap)-1]
            while True:
                if self.current*2 + 1 > len(self.heap)-1:  # 자식이 없는 경우 - stop
                    break
                elif self.current*2 + 2 > len(self.heap)-1:  # 왼쪽 자식만 있는 경우 - pop해서 없어질거니 stop
                    break
                elif self.current*2 + 2 == len(self.heap)-1:  # 오른쪽 자식이 끝일 경우 - 왼쪽 자식에 붙여줌 ###############
                    if self.temp < self.heap[self.current*2 + 1]:   # 내려가야할 경우
                        self.heap[self.current] = self.heap[self.current*2 + 1]
                        self.current = self.current*2 + 1
                    break
                if self.heap[self.current*2 + 1] > self.heap[self.current*2 + 2]: # 왼쪽 자식이 큰 경우 왼쪽으로 내려감
                    if self.heap[self.current*2 + 1] > self.temp:
                        self.heap[self.current] = self.heap[self.current*2 + 1]
                        self.current = self.current*2 + 1
                    else: break
                else:
                    if self.heap[self.current*2 + 2] > self.temp:
                        self.heap[self.current] = self.heap[self.current*2 + 2] # 아니면 오른쪽
                        self.current = self.current*2 + 2
                    else: break
            self.heap[self.current] = self.temp
            self.heap.pop()
            return x
        else:
            return 0


heap_q = HeapQueue()
for _ in range(num):
    input_num = int(sys.stdin.readline())
    if input_num > 0:
        heap_q.push(input_num)
        print(heap_q.heap)
    else:
        ans = heap_q.pop()
        print(heap_q.heap)
        print(ans)
