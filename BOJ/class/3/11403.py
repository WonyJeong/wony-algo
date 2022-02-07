import sys
input = sys.stdin.readline

def bfs(N,i, dic,answer):
    _answer = answer
    visited = [False for _ in range(N)]
    stack = [i]
    while stack:
        top = stack.pop()
        if not visited[top]:
            visited[top] = True
            if top in dic:
                for _next in dic[top]:
                    stack.append(_next)
                    _answer[i][_next] = 1
    return _answer

def solution(N, arr):
    answer = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        answer = bfs(N,i,dic,answer)

    print('\n'.join((' '.join(str(v) for v in row) for row in answer)))

if __name__ == '__main__':
    N = int(input().strip())
    arr = []
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        arr.append(row)
    dic = {}
    for u in range(N):
        for v in range(N):
            if arr[u][v] == 1:
                if not u in dic:
                    dic[u] = []
                dic[u].append(v)
    solution(N, dic)