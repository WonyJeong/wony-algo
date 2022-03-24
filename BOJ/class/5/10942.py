import sys
input = sys.stdin.readline

def solution(n, arr):
    dp = [[False for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = True
        if i > 0 and arr[i] == arr[i-1]:
            dp[i-1][i] = True
    for i in range(2, n):
        for j in range(n - i):
            if arr[j] == arr[j+i] and dp[j+1][j+i-1]:
                dp[j][j + i] = True
    return dp
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    m = int(input().strip())
    dp = solution(n, arr)
    for _ in range(m):
        s, e = map(int, input().strip().split())
        print(1 if dp[s-1][e-1] else 0)
