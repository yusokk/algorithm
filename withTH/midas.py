# def solution(N, mine):
#     board = list([0] * N for _ in range(N))
#     dr = [1, 1, 1, 0, 0, -1, -1, -1]
#     dc = [-1, 0, 1, -1, 1, -1, 0, 1]
#
#     for r, c in mine:
#         board[r - 1][c - 1] = -1
#
#     for r, c in mine:
#         for i in range(8):
#             adjacent_r = (r - 1) + dr[i]
#             adjacent_c = (c - 1) + dc[i]
#
#             if 0 <= adjacent_r < N and 0 <= adjacent_c < N:
#                 if board[adjacent_r][adjacent_c] == -1:
#                     continue
#                 board[adjacent_r][adjacent_c] += 1
#
#     return board

##############################################################

# def solution(n, v1, v2, num, amount):
#     leaders = [i for i in range(n + 1)]
#     team_dict = {}
#
#     def find_leader(member):
#         if leaders[member] == member:
#             return member
#         leaders[member] = find_leader(leaders[member])
#         return leaders[member]
#
#     def union(member1, member2):
#         leader1 = find_leader(member1)
#         leader2 = find_leader(member2)
#         if leader1 == leader2:
#             return
#         if leader1 < leader2:
#             leaders[leader2] = leader1
#         else:
#             leaders[leader1] = leader2
#
#     for i in range(len(v1)):
#         union(v1[i], v2[i])
#
#     for student in range(1, n+1):
#         team_leader = find_leader(student)
#         if not team_dict.get(team_leader, 0):
#             team_dict[team_leader] = 0
#
#     for i in range(len(num)):
#         team_leader = find_leader(num[i])
#         team_dict[team_leader] += amount[i]
#
#     best_score = -100000
#     best_leader = 10001
#     for current_leader, current_score in team_dict.items():
#         if current_score > best_score:
#             best_score = current_score
#             best_leader = current_leader
#         elif current_score == best_score and current_leader < best_leader:
#             best_leader = current_leader
#
#     print(best_leader)
#     return best_leader
# #
# solution(4,	[1, 3],	[2, 4],	[2, 2],	[1, -2])

#####################################################################


# def solution(N, K, T):
#     calender = list(0 for _ in range(K + 1))
#     prefer = {}
#
#     for t in T:
#         for i in range(t[0], t[1] + 1):
#             if not prefer.get(i, 0):
#                 prefer[i] = 0
#             prefer[i] += 1
#
#     sorted_T = sorted(T, key=lambda x: x[1] - x[0])
#
#     for t in sorted_T:
#         reservation = 0
#         date_prefer = N
#         for i in range(t[0], t[1] + 1):
#             if not calender[i] and prefer[i] < date_prefer:
#                 date_prefer = prefer[i]
#                 reservation = i
#             prefer[i] -= 1
#         if reservation:
#             calender[reservation] = 1
#
#     return calender.count(1)