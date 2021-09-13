d = [0, 0, 1, -1]
visit = []
table_visit = []

# dfs로 도형 고르기
def find_target(r, c, board, target, visit):
    cnt = 0
    min_r, max_r, min_c, max_c = r, r, c, c

    history = []
    stack = [[r, c]]
    while stack:
        pop_r, pop_c = stack.pop()
        if pop_r * len(board) + pop_c in visit:
            continue

        cnt += 1
        history.append([pop_r, pop_c])
        visit.append(pop_r * len(board) + pop_c)

        min_r = min(min_r, pop_r)
        max_r = max(max_r, pop_r)
        min_c = min(min_c, pop_c)
        max_c = max(max_c, pop_c)

        for i in range(4):
            next_r, next_c = pop_r + d[i], pop_c + d[3 - i]
            if 0 <= next_r < len(board) and 0 <= next_c < len(board):
                if next_r * len(board) + next_c in visit:
                    continue
                if board[next_r][next_c] == target:
                    stack.append([next_r, next_c])

    # 해당 도형만 포함하는 직사각형을 리턴해주기 위함
    ret_board = list(list(0 for _ in range(max_c - min_c + 1)) for _ in range(max_r - min_r + 1))
    for coord in history:
        ret_board[coord[0] - min_r][coord[1] - min_c] = 1

    return [cnt, ret_board]

# 시계방향으로 돌림
def clock_wise(target):
    return list(list(target[j][i] for j in range(len(target)-1, -1, -1)) for i in range(len(target[0])))

# 4방향에 대해서 일치하는지 비교
def compare(target, goal):
    target_1 = target
    target_2 = clock_wise(target_1)
    target_3 = clock_wise(target_2)
    target_4 = clock_wise(target_3)
    targets = [target_1, target_2, target_3, target_4]

    for t in targets:
        if t == goal:
            return True

    return False


def solution(game_board, table):
    answer = 0

    # 게임보드에서 빈칸 추출
    targets = []
    for r in range(len(game_board)):
        for c in range(len(game_board)):
            if game_board[r][c] == 0 and r * len(game_board) + c not in visit:
                targets.append(find_target(r, c, game_board, 0, visit))

    # 테이블에서 도형 추출
    blocks = {}
    for r in range(len(table)):
        for c in range(len(table)):
            if table[r][c] == 1 and r *len(table) + c not in table_visit:
                target = find_target(r, c, table, 1, table_visit)
                if not blocks.get(target[0], 0):
                    blocks[target[0]] = []
                blocks[target[0]].append(target[1])

    # 도형과 빈칸 비교
    for target in targets:
        target_blocks = blocks.get(target[0], 0)
        if not target_blocks:
            continue
        for i in range(len(target_blocks)):
            if compare(target_blocks[i], target[1]):
                answer += target[0]
                blocks[target[0]].pop(i)
                break

    print(answer)
    return answer


# solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
# solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]])
# solution([[0,1,0,1], [0,1,0,0], [0,1,1,1], [0,0,0,0]], [[1,0,0,0], [1,0,0,0],[1,0,0,0],[1,1,1,1]])
# solution([[1, 0, 1], [0, 1, 0], [1, 0, 1]], [[1, 0, 1], [0,1,0], [1,0,1]])
# solution([[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[1,1,1],[1,1,1]])