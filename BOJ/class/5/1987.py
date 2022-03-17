import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]; dy = [0, -1, 0, 1]
def solution(x,y,depth):
    global answer
    _ord = ord(board[x][y]) - 65
    if not visited[_ord]:
        answer = max(answer, depth)
        if answer >= 26: return
        visited[_ord] = True
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[ord(board[nx][ny]) - 65]:
                solution(nx,ny,depth+1)
                visited[ord(board[nx][ny]) - 65] = False

if __name__ == '__main__':
    global n, m, board, visited, answer
    answer = 0; n, m = map(int, input().strip().split()); board = []; visited = set();
    visited = [False for _ in range(26)]
    for _ in range(n): board.append(input().strip())
    solution(0, 0, 1); print(answer)