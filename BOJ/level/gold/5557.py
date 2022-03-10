import sys
input = sys.stdin.readline

def solution(N, arr):
    dp = [[0 for _ in range(21)] for _ in range(N-1)]
    dp[0][arr[0]] = 1
    for i in range(1, N-1):
        for j in range(0, 21):
            if dp[i-1][j] > 0:
                if 0 <= (arr[i] + j)  <= 20:
                    dp[i][arr[i] + j] += dp[i-1][j]
                if 0 <= (j - arr[i]) <= 20:
                    dp[i][j - arr[i]] += dp[i-1][j]
    print(dp[-1][arr[-1]])
                

if __name__ == '__main__':
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(N, arr)