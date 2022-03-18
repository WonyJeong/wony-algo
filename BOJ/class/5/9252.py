import sys
input = sys.stdin.readline
def solution(str1, str2):
    dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2) + 1)]
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str1[j-1] == str2[i-1]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    answer = ''; i = len(str2); j = len(str1)
    for r in dp:
        print(r)
    while len(answer) < dp[len(str2)][len(str1)]:
        print(i, j)
        if str2[i-1] == str1[j-1]:
            answer = str2[i-1] + answer
            i -= 1; j -= 1
        else:
            if dp[i][j-1] > dp[i-1][j]: j -= 1
            else: i -= 1
    print(dp[len(str2)][len(str1)])
    print(answer)
if __name__ == "__main__":
    str1 = input().strip(); str2 = input().strip()
    solution(str1, str2)