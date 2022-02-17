import sys
from itertools import permutations
input = sys.stdin.readline

def solution(N, M, _arr):
    arr = sorted(_arr)
    for per in permutations(arr, M):
        print(' '.join(str(v) for v in list(per))) 

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    solution(N, M, arr)



