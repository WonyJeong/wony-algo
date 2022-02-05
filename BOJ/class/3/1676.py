import sys
input = sys.stdin.readline

def solution(_n):
    answer = 0
    value = 1
    n = _n

    while n:
        value *= n
        if value % 10 == 0:
            answer += 1
            value = value // 10
        n -= 1

    print(answer)

if __name__ == '__main__':
    solution(int(input().strip()))