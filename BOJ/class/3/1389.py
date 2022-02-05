import sys
from collections import deque
input = sys.stdin.readline

def bfs(dic, N, start):
    visited = [False for _ in range(N+1)]
    step = [0 for _ in range(N+1)]
    q = deque([start])
    while q:
        node = q.popleft()
        if not visited[node]:
            visited[node] = True
            if node in dic:
                for v in dic[node]:
                    q.append(v)
                    if step[v] == 0 and not v == start:
                        step[v] = step[node] + 1
    return sum(step)

def solution(dic,N):
    answer = [-1, sys.maxsize]
    for start in range(1, N+1):
        total = bfs(dic, N, start)
        if answer[1] > total : answer = [start, total]

    print(answer[0])
    return answer

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    dic = {}
    for _ in range(M):
        u, v = map(int, input().strip().split())
        if not u in dic:
            dic[u] = []
        if not v in dic:
            dic[v] = []
        dic[u].append(v)
        dic[v].append(u)
    solution(dic, N)