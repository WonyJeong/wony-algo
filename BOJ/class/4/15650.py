from itertools import combinations
import sys

input = sys.stdin.readline

def solution(n,m):
    for comb in combinations([i for i in range(1, n+1)], m):
        comb = list(comb)
        print(' '.join(str(c) for c in comb))

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    solution(n,m)