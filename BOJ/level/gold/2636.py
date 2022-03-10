from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def counter(arr):
    ct = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]: ct += 1
    return ct

def bfs(i, j, arr, _new_arr):
    new_arr = _new_arr
    q = deque([(i, j)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    while q:
        x, y = q.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:    
                    if arr[nx][ny] == 1:
                        new_arr[nx][ny] = 0
                    else:
                        q.append((nx, ny))
    return new_arr


def solution(N, M, _arr):
    time, last = 0, counter(_arr)
    arr = _arr
    while True:
        time += 1
        new_arr = deepcopy(arr)       
        arr = bfs(0, 0, arr, new_arr)
        temp = counter(arr)
        if not temp:
            print(time)
            print(last)
            return
        last = temp
        
if __name__ == '__main__':
    global N, M
    N, M = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(N, M, arr)
