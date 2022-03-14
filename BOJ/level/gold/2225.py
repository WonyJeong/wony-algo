import sys
input = sys.stdin.readline

def solution(n, k):
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(n+1): dp[1][i] = 1

    for i in range(1,k+1):
        for j in range(n+1):
            for l in range(j+1):
                dp[i][j] += dp[i-1][j-l]
                dp[i][j] %= 1000000000
    print(dp[k][n])

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    solution(n, k)