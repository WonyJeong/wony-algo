import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, dic, visited):
    q = deque([i])
    _visited = visited
    while q:
        bottom = q.popleft()
        if not _visited[bottom]:
            _visited[bottom] = True
            if bottom in dic:
                for v in dic[bottom]:
                    q.append(v)
    return _visited

def solution(dic, N, M):
    answer = 0
    visited = [False for _ in range(N+1)]

    for i in range(1, N+1):
        if not visited[i]:
            visited = bfs(i,dic, visited)
            answer += 1

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
    print(solution(dic, N,M))
        