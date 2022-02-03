import sys
input = sys.stdin.readline


def coordinate(N,r,c):
    if N == 1:
        return N,r,c

    x = r >= pow(2,N)/2
    y = c >= pow(2,N)/2
    temp = pow(2,N)/2

    if not x and not y:
        return N-1, r, c, 0
    elif not x and y:
        return N-1, r, c-temp, 1
    elif x and not y:
        return N-1, r-temp, c, 2
    else:
        return N-1, r-temp, c-temp, 3

def solution(_N, _r, _c):
    N, r, c = _N, _r, _c
    answer = 0
    for _ in range(_N-1):
        temp = pow(4,N) / 4 
        N, r, c, loc = coordinate(N,r,c)
        answer += loc * temp
    if r == 0 and c == 1:
        answer += 1
    elif r == 1 and c ==0:
        answer += 2
    elif r == 1 and c ==1:
        answer += 3

    return round(answer)

if __name__ == '__main__':
    N, r, c = map(int, input().strip().split())
    print(solution(N, r, c))
    