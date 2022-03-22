import sys
input = sys.stdin.readline

mod = 10000000000

def solution(i, j, k):
    if j < 0 or j > 9: return 0
    if i == n:
        if k == 1023: return 1
        else: return 0

    if dp[i][j][k] != -1:
        return dp[i][j][k]

    dp[i][j][k] = 0
    if 0 < j < 9:
        plus_nbit = k | (1 << (j + 1)); minus_nbit = k | (1 << (j - 1))
        dp[i][j][k] += solution(i+1, j+1, plus_nbit); 
        dp[i][j][k] %= mod
        dp[i][j][k] += solution(i+1, j-1, minus_nbit); 
        dp[i][j][k] %= mod
    elif j == 0:
        plus_nbit = k | (1 << (j + 1));
        dp[i][j][k] += solution(i+1, j+1, plus_nbit); 
        dp[i][j][k] %= mod
    else:
        minus_nbit = k | (1 << (j - 1))
        dp[i][j][k] += solution(i+1, j-1, minus_nbit); 
        dp[i][j][k] %= mod

    return dp[i][j][k]

if __name__ == '__main__':
    global dp, n
    n = int(input().strip())
    answer = 0
    dp = [[[-1 for _ in range(1024)] for _ in range(10)] for _ in range(n+1)]
    for i in range(1, 10):
        answer += solution(1, i, 1<<i)
        answer %= mod
    print(answer)
