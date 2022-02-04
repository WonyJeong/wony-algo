import sys
input = sys.stdin.readline

def solution(dic, arr):
    for cmd in arr:
        print(dic[cmd])

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    dic = {}
    arr = []
    for i in range(1, N+1):
        temp = str(input().strip())
        dic[temp] = str(i)
        dic[str(i)] = temp
    for _ in range(M):
        arr.append(str(input().strip()))
    solution(dic, arr)