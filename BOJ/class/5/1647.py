import heapq
import sys
input = sys.stdin.readline

def solution(start):
    q = []; visited = set(); visited.add(start)
    answer = 0; ct = 1; max_weight = -1
    for v, w in graph[start]:
        heapq.heappush(q, (w, v))
    while ct != n:
        while q:
            w, v = heapq.heappop(q)
            if not v in visited : break
        visited.add(v); ct += 1
        answer += w; max_weight = max(max_weight, w)
        for _v, _w in graph[v]:
            heapq.heappush(q, (_w, _v))
    print(answer - max_weight)

if __name__ == '__main__':
    global n, m, graph
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    solution(1)