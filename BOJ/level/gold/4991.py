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
        if bit + 1 == 1 << dirty:
            print(count); return;
        if not visited[bit][x][y]:
            visited[bit][x][y] = True
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != 'x':
                    if arr[nx][ny] == 'o' or arr[nx][ny] == '.':
                        q.append((bit,nx,ny,count+1))
                    else:
                        shift = int(arr[nx][ny])
                        nbit = bit + (1 << shift) if not bit & (1 << shift) else bit
                        q.append((nbit,nx,ny,count+1))
    print(-1)

def solution(w,h,arr):
    global visited, dirty
    dirty = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'o':
                x = i; y = j
            if arr[i][j] == '*':
                arr[i][j] = str(dirty)
                dirty += 1
    visited = [[[False for _ in range(w)] for _ in range(h)] for _ in range(1 << dirty)]
    bfs(x, y)

if __name__ == '__main__':
    global w, h, arr
    while True:
        w, h = map(int, input().strip().split())
        if w == 0 and h == 0:
            break
        arr = []
        for _ in range(h):
            arr.append(list(map(str, input().strip())))
        solution(w,h,arr)
