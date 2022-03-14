from collections import deque
from math import inf
import sys
input = sys.stdin.readline

def solution(n):
    q = deque([(0,1,0)])
    dp = [[inf for _ in range(3002)] for _ in range(3002)]
    while q:
        board, screen, time = q.popleft()
        if screen == n:
            print(time)
            return
        if 0 <= board <= 3002 and 0 <= screen <= 3002 and dp[board][screen] > time:
            dp[board][screen] = time
            q.append((screen, screen, time + 1))
            if screen + board < 1002:
                q.append((board, screen + board, time + 1))
            if screen - 1 >= 0:
                q.append((board, screen - 1, time + 1))

if __name__ == '__main__':
    n = int(input().strip())
    solution(n)