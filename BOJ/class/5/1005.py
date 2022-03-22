from collections import deque
from copy import deepcopy
from math import inf
import sys
input = sys.stdin.readline
# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#       ① 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
#       ② 새롭게 진입차수가 0이 된 노드를 큐에 삽입
def solution(n, k, cost, graph, w, in_degree):
    dp = [0 for _ in range(n)]; topology = deque([]); q = deque([])
    _graph = deepcopy(graph)
    for i in range(n): 
        if not in_degree[i]: q.append((i, 0));
    while q:
        node, depth = q.popleft()
        topology.append((node, depth))
        while _graph[node]:
            next = _graph[node].pop()
            in_degree[next] -= 1
            if not in_degree[next]: q.append((next, depth + 1));
    while topology:
        node, depth = topology.popleft()
        dp[node] += cost[node]
        for next in graph[node]:
            dp[next] = max(dp[next], dp[node])
    return dp[w]

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n, k = map(int, input().strip().split())
        graph = [[] for _ in range(n)]
        cost = list(map(int, input().strip().split()))
        in_degree = [0 for _ in range(n)]
        for _ in range(k):
            u, v = map(int, input().strip().split())
            u -= 1; v -= 1;
            graph[u].append(v)
            in_degree[v] += 1
        w = int(input().strip()); w -= 1
        print(solution(n, k, cost, graph, w, in_degree))