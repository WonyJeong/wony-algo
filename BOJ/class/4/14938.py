import sys
import heapq
from math import inf
input = sys.stdin.readline

def dijkstra(n, dic, start_node):
    dist = [inf for _ in range(n+1)]    
    dist[start_node] = 0
    q = []
    heapq.heappush(q, (0, start_node))
    while q:
        d, current = heapq.heappop(q)
        if current in dic:
            for v, l in dic[current]:
                if dist[v] > d + l:
                    dist[v] = d + l
                    heapq.heappush(q, (d+l, v))
    return dist

def solution(n, m, item, dic):
    answer = 0
    for i in range(1, n + 1):
        dist = dijkstra(n, dic, i)
        temp = 0
        for j in range(n):
            if dist[j+1] <= m:
                temp += item[j]
        answer = max(answer, temp)

    print(answer)
    return answer

if __name__ == '__main__':
    n, m, r = map(int, input().strip().split())
    item = list(map(int, input().strip().split()))
    dic = {}
    for _ in range(r):
        a, b, l = map(int, input().strip().split())
        if a not in dic:
            dic[a] = []
        if b not in dic:
            dic[b] = []
        dic[a].append((b,l))
        dic[b].append((a,l))
    
    solution(n, m, item, dic)