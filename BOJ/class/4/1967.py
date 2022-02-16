import sys
input = sys.stdin.readline

# 임의의 노드(모든 경우는, 1을 루트 노드로 가진다는 가정이 있으므로 노드 1로 설정)로 부터 가장 멀리있는 노드 A를 dfs로 탐색
# A에서 가장 멀리있는 노드 B를 탐색하고 그 거리(원의 지름)을 반환

def dfs(start, n, dic):
    visited = [False for _ in range(n+1)]
    dist = [-1 for _ in range(n+1)]
    dist[start] = 0
    stack = [(start, 0)]
    while stack:
        node, w =  stack.pop()
        if not visited[node]:
            visited[node] = True
            if node in dic:
                for next_node in dic[node]:
                    v, k = next_node
                    stack.append((v, w + k))
                    if dist[v] == -1:
                        dist[v] = w + k
    return dist

def solution(n, dic):
    start_node = -1
    answer = 0
    dist = dfs(1, n, dic)
    for i in range(1, n+1):
        if answer < dist[i]:
            start_node = i
            answer = dist[i]


    dist = dfs(start_node, n , dic)
    for i in range(1, n+1):
        if answer < dist[i]:
            answer = dist[i]

    print(answer)


if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    for _ in range(n-1):
        u, v, w = map(int, input().strip().split())
        u = u
        v = v
        if not u in dic:
            dic[u] = set()
        if not v in dic:
            dic[v] = set()
        dic[u].add((v,w))
        dic[v].add((u,w))
    solution(n, dic)