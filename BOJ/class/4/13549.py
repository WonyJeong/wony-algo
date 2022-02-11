from collections import deque
import heapq
from math import inf
import sys
input = sys.stdin.readline

def solution(n,k):
    memo = [inf for _ in range(100001)]
    visited = [False for _ in range(100001)]
    q = [(0, n)]
    memo[n] = 0
    while q:
        current = heapq.heappop(q)[1]
        if current == k:
            print(memo[k])
            return memo[k]
        
        if visited[current] == False:
            visited[current] = True

            temp = current
            while 0 < temp < k+2:
                memo[temp] = memo[current]
                heapq.heappush(q, (memo[temp], temp))
                temp *= 2
            
            if current > 0:
                time = min(memo[current] + 1, memo[current - 1])
                heapq.heappush(q, (time, current - 1))
                memo[current-1] = time

            if current < k:
                time = min(memo[current] + 1, memo[current + 1])
                heapq.heappush(q, (time, current + 1))
                memo[current+1] = time
        
if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    solution(n,k)