import heapq
import sys
input = sys.stdin.readline

# 최소신장트리 (MST, 프림알고리즘)

def solution(start):
    q = []; visited = set(); visited.add(start)
    answer = 0; ct = 1;
    for v, w in graph[start]:
        heapq.heappush(q, (w, v))
    while ct != n:
        while q:
            w, v = heapq.heappop(q)
            if not v in visited : break
        visited.add(v); ct += 1
        answer += w;
        for _v, _w in graph[v]:
            heapq.heappush(q, (_w, _v))
    print(answer)

if __name__ == '__main__':
    global n, m, graph
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    solution(1)