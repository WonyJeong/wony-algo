import heapq
from itertools import permutations
from math import inf

dstr = ['left', 'right', 'down', 'up']
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def ctrl_move(x,y,k, board):
    nx , ny = x, y
    while True:
        if k == 'left':
            if ny > 0:
                ny -= 1
            if (board[nx][ny] != 0 and checked_board[nx][ny] == False) or ny == 0:
                break
        elif k == 'right':
            if ny < 3:
                ny += 1
            if (board[nx][ny] != 0 and checked_board[nx][ny] == False) or ny == 3:
                break            
        elif k == 'up':
            if nx > 0:
                nx -= 1
            if (board[nx][ny] != 0 and checked_board[nx][ny] == False) or nx == 0:
                break
        elif k == 'down':
            if nx < 3:
                nx += 1
            if (board[nx][ny] != 0 and checked_board[nx][ny] == False) or nx == 3:
                break

    if nx == x and ny == y:
        return -1, -1    
    return nx, ny

def card_search(r, c, pair_num):
    dist = [[inf for _ in range(4)] for _ in range(4)]
    dist[r][c] = 0
    q = []
    heapq.heappush(q, (0, r, c))
    while q:
        cost, x, y = heapq.heappop(q)
        if board[x][y] == pair_num and not checked_board[x][y]:
            return cost, x, y
        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 4 and 0 <= ny < 4 and dist[nx][ny] > cost + 1:
                dist[nx][ny] = cost + 1
                heapq.heappush(q, (cost+1, nx, ny))

        for k in dstr:
            nx, ny = ctrl_move(x, y, k, board)
            if nx != -1 and ny != -1 and dist[nx][ny] > cost + 1:
                dist[nx][ny] = cost + 1
                heapq.heappush(q, (cost+1, nx, ny))
        
def game_start(r, c, arr):
    x, y = r, c
    total_cost = 0
    for card_num in arr:
        search_cost, sx, sy = card_search(x, y, card_num)
        checked_board[sx][sy] = True
        pair_cost, nx, ny = card_search(sx, sy, card_num)
        checked_board[nx][ny] = True

        total_cost += search_cost + pair_cost + 2

        x, y = nx, ny
    return total_cost

def solution(_board, r, c):
    global board, checked_board
    board = _board
    answer = inf
    card_set = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_set.add(board[i][j])

    for arr in permutations(card_set):
        checked_board = [[False for _ in range(4)] for _ in range(4)]
        answer = min(answer , game_start(r, c, arr))

    return answer

if __name__ == '__main__':
    board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r = 1
    c = 0
    print(solution(board, r, c))
    