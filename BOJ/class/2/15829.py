import sys
input = sys.stdin.readline


def solution(L, str):
    answer = 0
    digt = 1
    for i in range(L):
        answer += (ord(str[i]) - 96) * digt
        digt *= 31

    print(answer % 1234567891)

if __name__ == '__main__':
    L = int(input().strip())
    str = input().strip()
    solution(L, str)