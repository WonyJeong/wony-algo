from collections import deque
import sys
input = sys.stdin.readline

# left,up,right,down
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def move(dir, a, b):
    ni, nj = a
    while True:
        if board[ni + dx[dir]][nj + dy[dir]] != '#' and (ni + dx[dir],nj + dy[dir]) != b:
            ni += dx[dir]; nj += dy[dir];
            if board[ni][nj] == 'O':
                return (-1, -1)
        else:
            return (ni, nj)

def find_position():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red = (i,j)
            if board[i][j] == 'B':
                blue= (i,j)
    return red, blue

def incline(dir, red, blue):
    red_first = True
    if dir == 'left':
        dir = 0
        if red[1] >= blue[1]: red_first = False
    elif dir == 'right':
        dir = 2
        if red[1] < blue[1]: red_first = False
    elif dir == 'up':
        dir = 1
        if red[0] > blue[0]: red_first = False
    elif dir == 'down':
        dir = 3
        if red[0] < blue[0]: red_first = False

    if red_first:
        red = move(dir, red, blue)
        blue = move(dir, blue, red)
    else:
        blue = move(dir, blue, red)
        red = move(dir, red, blue)
    return red, blue    
 

def bfs(red, blue):
    answer = -1
    vis = set()
    q = deque([[red, blue, 0]])
    while q:
        red, blue, depth = q.popleft()
        if red == (-1, -1) and blue != (-1, -1) and depth < 11:
            answer = depth
            break
        if depth > 10: continue
        if red + blue not in vis:
            vis.add(red + blue)
            for dir in ['left', 'right', 'up', 'down']:
                next_red, next_blue = incline(dir, red, blue);
                q.append([next_red, next_blue, depth + 1]);
    return answer

def solution():
    red, blue = find_position()
    return bfs(red, blue)

if __name__ == '__main__':
    global n, m, board
    n, m = map(int, input().strip().split())
    board = [list(map(str, input().strip())) for _ in range(n)]
    print(solution())

