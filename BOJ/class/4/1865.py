
import sys
input = sys.stdin.readline

def solution(N, edges):
    INF = 2147483647
    dist = [INF for _ in range(N+1)]
    dist[1] = 0
    for i in range(N):
        for current_node, next_node, edge_cost in edges:
            if dist[next_node] > dist[current_node] + edge_cost:
                dist[next_node] = dist[current_node] + edge_cost
                if i == N - 1:
                    return True
    return False

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N, M, W = map(int, input().strip().split())
        edges = []
        for _ in range(M):
            S, E, T = map(int, input().strip().split())
            edges.append((S,E,T))
            edges.append((E,S,T))
        for _ in range(W):
            S, E, T = map(int, input().strip().split())
            edges.append((S,E, -1 * T))

        print('YES') if solution(N, edges) else print('NO')