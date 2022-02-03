import sys
input = sys.stdin.readline

def solution(N,row):
    answer = 0
    dp = [True for _ in range(1001)]
    dp[1] = False
    for i in range(2, 101):
        if dp[i] == True:
            for j in range(i, 1001):
                if i*j < 101:
                    dp[i*j] = False
                else:
                    break
    
    for val in row:
        answer += 1 if dp[val] else 0
    
    return answer
    

if __name__ == '__main__':
    N = int(input().strip())
    row = list(map(int, input().strip().split()))
    print(solution(N,row))

