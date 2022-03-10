from collections import deque
import sys
input = sys.stdin.readline

def solution(n):
    dp = [0 for _ in range(len(n)+1)]
    dp[0] = 1
    for i in range(1, len(n) + 1):
        if n[i-1] != '0':
            dp[i] = (dp[i] + dp[i-1]) % 1000000
        if not i > 1:
            continue    
        temp = int(n[i-2]) * 10 + int(n[i-1])
        if 10 <= temp < 27:
            dp[i] = (dp[i] + dp[i-2]) % 1000000
    print(dp[-1] % 1000000)

if __name__ == '__main__':
    solution(input().strip())