from collections import deque
from math import inf
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(_x, _y):
    q = deque([(0, _x, _y, 0)])
    while q:
        bit, x, y, count = q.popleft()
        if arr[x][y] == '1':
            print(count); return;

        if not visited[bit][x][y]:
            visited[bit][x][y] = True
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '#':
                    if arr[nx][ny] == '0' or arr[nx][ny] == '.' or arr[nx][ny] == '1':
                        q.append((bit,nx,ny,count+1))
                    else:
                        if 0 <= ord(arr[nx][ny]) - 65 <= 5:
                            door = ord(arr[nx][ny]) - 65
                            if not bit & 1 << door: continue
                            q.append((bit,nx,ny,count+1))
                        if 0 <= ord(arr[nx][ny]) - 97 <= 5:
                            key = ord(arr[nx][ny]) - 97
                            nbit = bit + (1 << key) if not bit & (1 << key) else bit
                            q.append((nbit,nx,ny,count+1))
    print(-1)

def solution(w,h,arr):
    global visited, dirty
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '0':
                x = i; y = j
                break
    visited = [[[False for _ in range(w)] for _ in range(h)] for _ in range(1 << 6)]
    bfs(x, y)

if __name__ == '__main__':
    global w, h, arr
    h, w = map(int, input().strip().split())
    arr = []
    for _ in range(h):
        arr.append(list(map(str, input().strip())))
    solution(w,h,arr)