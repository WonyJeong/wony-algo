from math import inf
import sys
input = sys.stdin.readline


def dfs(N, start, dic):
    dist = [inf] * (N+1)
    visited = [False] * (N+1)
    dist[start] = 0

    stack = [(start, 0)]
    while stack:
        current, edge_cost = stack.pop()
        if not visited[current]:
            visited[current] = True
            if current in dic:
                for next_node, next_cost in dic[current]:
                    stack.append((next_node, next_cost + edge_cost))
                    if dist[next_node] == inf : dist[next_node] = next_cost + edge_cost
    
    return dist
        

def solution(N, dic):
    start_node = -1
    answer = 0
    dist = dfs(N, 1, dic)
    for i in range(1, N+1):
        if answer < dist[i]:
            start_node = i
            answer = dist[i]


    dist = dfs(N, start_node , dic)
    for i in range(1, N+1):
        if answer < dist[i]:
            answer = dist[i]

    print(answer)


if __name__ == '__main__':
    N = int(input().strip())
    dic = {}
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        if row[0] not in dic:
            dic[row[0]] = set()
        for i in range(1, len(row) - 1, 2):
            dic[row[0]].add((row[i], row[i+1]))
            if not row[i] in dic:
                dic[row[i]] = set()
            dic[row[i]].add((row[0], row[i+1]))

    solution(N, dic)


