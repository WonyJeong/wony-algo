import sys
input = sys.stdin.readline

def getLastYear(M,N):
    year = M
    while 1:
        cy = year % N if year % N != 0 else N
        if cy == N:
            return year
        year += M

def solution(M,N,x,y):
    answer = x
    last_year = getLastYear(M,N)

    while answer <= last_year:
        cy = answer % N if answer % N != 0 else N
        if cy == y:
            return answer
        answer += M
    return -1
        
if __name__ == '__main__':
    N = int(input().strip())
    for _ in range(N):
        M, N, x, y = map(int, input().strip().split())
        print(solution(M,N,x,y))
