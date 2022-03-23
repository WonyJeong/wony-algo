from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#       ① 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
#       ② 새롭게 진입차수가 0이 된 노드를 큐에 삽입
def solution(n, m, graph, in_degree):
    topology = deque([]); q = deque([])
    _graph = deepcopy(graph)
    answer = []
    for i in range(n): 
        if not in_degree[i]: q.append(i);
    while q:
        node = q.popleft()
        topology.append(node)
        while _graph[node]:
            next = _graph[node].pop()
            in_degree[next] -= 1
            if not in_degree[next]: q.append(next);

    while topology:
        node = topology.popleft()
        answer.append(str(node+1))
    
    print(' '.join(v for v in answer))

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n)]
    in_degree = [0 for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().strip().split())
        u -=1; v -=1;
        in_degree[v] += 1
        graph[u].append(v)
    solution(n, m, graph, in_degree)


