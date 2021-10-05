from collections import deque
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    pre = []
    post = []
    sorted_info = deque(sorted(map(lambda x: [x[0]+1, x[1][0], x[1][1]], enumerate(nodeinfo)), key=lambda x: (-x[2], x[1])))

    def split(que):
        if not que:
            return
        parent, parent_x, parent_y = que.popleft()

        left = deque(filter(lambda x: x[1] < parent_x, que))
        right = deque(filter(lambda x: x[1] > parent_x, que))

        pre.append(parent)
        split(left)
        split(right)
        post.append(parent)

    split(sorted_info)
    answer = [pre, post]

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]] ))
print(solution([[1,2], [2, 3]]))
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]