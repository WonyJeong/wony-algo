from collections import deque
from math import inf
import sys
input = sys.stdin.readline

def solution(n,k):
    count = 0
    memo = [inf for _ in range(100001)]
    q = deque([(0, n)])
    flag = inf
    while q:
        t, current = q.popleft()
        if t > flag:
            break
        if current == k:
            count += 1
            flag = t

        if memo[current] >= t:
            memo[current] = t
            if 0 < current:
                q.append([t+1, current-1])
            if current < 100000:
                q.append([t+1, current+1]) 
            if current * 2 < 100001:
                q.append([t+1, current * 2])

    print(flag)
    print(count)

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    solution(n,k)