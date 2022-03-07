from collections import deque
import sys
input = sys.stdin.readline

dx = [0,-1,0,1]; dy = [-1,0,1,0]

def solution():
    q = deque([(x1,y1)])
    dist = [[-1 for _ in range(M)] for _ in range(N)]
    dist[x1][y1] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            for k in range(1, K+1):
                nx = x + dx[i] * k
                ny = y + dy[i] * k
                if not(0 <= nx < N and 0 <= ny < M and arr[nx][ny] != '#'): break
                # 방문 했는데, 최단 거리가 아니면 중단
                if -1 != dist[nx][ny] <= dist[x][y] : break

                if -1 != dist[nx][ny]: continue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    print(dist[x2][y2])

if __name__ == '__main__':
    global N, M, K, arr, x1, x2, y1, y2
    N, M, K = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(input().strip())
    x1, y1, x2, y2 = map(int, input().strip().split())
    x1 -= 1; x2 -= 1; y1 -= 1; y2 -= 1
    solution()