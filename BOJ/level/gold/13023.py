import sys
input = sys.stdin.readline

def bfs(n, start, dic):
    stack = [(start, [False for _ in range(n)])]
    while stack:
        current, visited = stack.pop()

        if v


    return

def solution(n, dic):
    for i in range(n):
        bfs(n, i, dic)


if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    for _ in range(n):
        u, v = map(int, input().strip().split())
        if u not in dic: dic[u] = set()
        if v not in dic: dic[v] = set()
        dic[u].add(v); dic[v].add(u);
    solution(n, dic)
