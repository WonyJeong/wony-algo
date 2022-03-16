import sys
input = sys.stdin.readline

def dfs(node, depth):
    global answer
    visited[node] = True
    if depth >= 4:
        answer = True
        return
    if node in dic:
        for v in dic[node]:
            if not visited[v]:
                dfs(v, depth + 1)
                visited[v] = False

def solution():
    global visited, answer
    answer = False
    visited = [False for _ in range(n)]
    for i in range(n):
        dfs(i, 0)
        if answer:
            print(1)
            return
        visited[i] = False
    print(0)


if __name__ == '__main__':
    global n, dic
    n, m = map(int, input().strip().split()) 
    dic = {}
    for _ in range(m):
        u, v = map(int, input().strip().split())
        if u not in dic: dic[u] = set()
        if v not in dic: dic[v] = set()
        dic[u].add(v); dic[v].add(u);
    solution()
