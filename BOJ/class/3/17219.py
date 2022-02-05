import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    dic = {}
    for _ in range(N):
        site, pw = map(str, input().strip().split())
        dic[site] = pw
    
    for _ in range(M):
        print(dic[input().strip()])
