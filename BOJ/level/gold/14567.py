from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, arr, answer):
    q = deque([(start, 0)])
    depth = 0
    while q:
        node, count = q.popleft()
        if answer[node] != -1:
            depth = max(depth, answer[node] + 1)
            continue
        for next in arr[node]:
            q.append((next, count + 1))

    return depth

def solution(n, arr):
    answer = [-1 for _ in range(n+1)]
    for i in range(1, n+1):
        answer[i] = bfs(i, arr, answer)
    print(' '.join(str(answer[i]+1) for i in range(1, n+1)))
    
if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().strip().split())
        arr[B].append(A)
    solution(N, arr)
        