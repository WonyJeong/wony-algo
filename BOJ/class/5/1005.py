from collections import deque
from math import inf
import sys
input = sys.stdin.readline

def solution(n, k, cost, graph, w, order):
    dist = [[] for _ in range(n)]
    topology = deque([]); q = deque([])
    vis = [False for _ in range(n)]

# 1. 진입차수가 0인 노드를 큐에 넣는다.

# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#       ① 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
#       ② 새롭게 진입차수가 0이 된 노드를 큐에 삽입

    for i in range(n):
        if not order[i]: q.append((i, 0));
    while q:
        node, depth = q.popleft()
        if vis[node]: continue
        topology.append((node, depth))
        vis[node] = True
        for next in graph[node]:
            q.append((next, depth + 1))
    print('topology : ', topology)


    answer = 0
    while topology:
        node, depth = topology.popleft()
        dist[depth].append(cost[node])
        if node == w:
            for i in range(depth):
                answer += max(dist[i])
            answer += cost[node]
    
    print('answer : ', answer)
    return

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n, k = map(int, input().strip().split())
        graph = [[] for _ in range(n)]
        cost = list(map(int, input().strip().split()))
        
        temp = [False for _ in range(n)]
        for _ in range(k):
            u, v = map(int, input().strip().split())
            u -= 1; v -= 1;
            graph[u].append(v)
            temp[v] = True
        w = int(input().strip()); w -= 1
        solution(n, k, cost, graph, w, temp)