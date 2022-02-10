from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(N, arr, i, j, visited, _type):
    _visited = visited
    q = deque([[i,j]])
    while q:
        x, y = q.popleft()
        current_color = arr[x][y]
        if not _visited[x][y]:
            _visited[x][y] = True
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0<= ny < N and _visited[nx][ny] == False:
                    next_color = arr[nx][ny]
                    if _type: # 색맹 아님
                        if current_color == next_color: 
                            q.append([nx,ny])
                    if not _type: # 색맹
                        if current_color == 'R' and next_color == 'G' or current_color == 'G' and next_color == 'R' or current_color == next_color:
                            q.append((nx,ny))
    return _visited

def temp():
    return [i for i in range(10)]

def solution(N, arr):
    x_visited = [[False for _ in range(N)] for _ in range(N)]
    y_visited = [[False for _ in range(N)] for _ in range(N)]

    x_answer, y_answer = 0, 0

    for i in range(N):
        for j in range(N):
            if not x_visited[i][j]:
                x_answer += 1
                x_visited = bfs(N, arr, i, j, x_visited, True)
            if not y_visited[i][j]:
                y_answer += 1
                y_visited = bfs(N, arr, i, j, y_visited, False)

    print(x_answer, y_answer)

if __name__ == '__main__':
    T = int(input().strip())
    arr = []
    for _ in range(T):
        arr.append(input().strip())
    solution(T, arr)
