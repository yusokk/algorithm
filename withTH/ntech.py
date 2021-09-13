# def solution(n):
#     max_mul = 1

#     for i in range(2, n+1):

#         # n: 주어진 수, i: 덧셈으로 표현할 갯수
#         # i개로 나눴을 때 최대한 비슷한 차이로 동등하게 분배해야 그 갯수에서 최대의 곱이 나옴
#         # 그러므로 나머지가 있으면 몫에 1만큼 나머지 갯수만큼 올려주면 됨
#         # ex) 8 % 3 = 2 + 2 -> 8을 3부분으로 나눌 것이다.
#         # 나머지 2만큼 2+1을 해줘서 3이 두개이고, 2가 1개 3+3+2가 3개로 나눴을 때 곱이 최대임

#         q, r = divmod(n, i)
#
#         if r:
#             current_mul = ((q+1) ** r) * (q ** (i-r))
#         else:
#             current_mul = q ** i
#
#         if max_mul < current_mul:
#             max_mul = current_mul
#
#     print(max_mul)
#     return max_mul
#
# solution(10)