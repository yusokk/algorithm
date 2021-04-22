import sys
from itertools import combinations
read = sys.stdin.readline

def blackjack(m, iter):
    comb_sum = list(sum(c) if sum(c) <= m else 0 for c in combinations(iter, 3))
    print(max(comb_sum))

N, M = map(int, read().rstrip().split())
cards = map(int, read().rstrip().split())
blackjack(M, cards)