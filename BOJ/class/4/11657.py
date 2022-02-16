
import sys
input = sys.stdin.readline

def solution(N, edges):
    INF = 2147483647
    dist = [INF for _ in range(N+1)]
    dist[1] = 0
    for i in range(N):
        for current_node, next_node, edge_cost in edges:
            if dist[current_node] != INF and dist[next_node] > dist[current_node] + edge_cost:
                dist[next_node] = dist[current_node] + edge_cost
                if i == N - 1:
                    print(-1)
                    return
    
    for i in range(2, N+1):
        print(dist[i]) if dist[i] != INF else print(-1)

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        edges.append((u,v,w))
    solution(N, edges)