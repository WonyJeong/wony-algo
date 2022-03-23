import sys
input = sys.stdin.readline

def find_position():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red = (i,j)
            if board[i][j] == 'B':
                blue= (i,j)
    return red, blue


def incline(dir, red, blue):
    if red[0] <= blue[0]:
        a = red; b = blue;
    else:
        b = red; a = blue;

    if red[1] <= blue[1]:
        c = red; d = blue;
    else:
        d = red; c = blue;

    if dir == 'left':
        x, y = a
        while True:
            if board[x][y-1] == '.' and b != (x, y-1):
                y -= 1
            else:
                a = (x, y)
                break
        x, y = b
        while True:
            if board[x][y-1] == '.' and a != (x, y-1):
                y -= 1
            else:
                b = (x, y)
                break
        return a, b
    elif dir == 'right':
        print()
    elif dir == 'up':
        print()
    elif dir == 'down':
        print()
    

def bfs(red, blue):
    print()
    


def solution():
    red, blue = find_position()


    return

if __name__ == '__main__':
    global n, m, board
    n, m = map(int, input().strip().split())
    board = [list(map(str, input().strip())) for _ in range(n)]
    solution(n, m, board)

