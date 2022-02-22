import sys
input = sys.stdin.readline

def solution(board, skill):
    answer = 0
    row_len = len(board[0])
    col_len = len(board)
    arr = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for _type, r1, c1, r2, c2, degree in skill:
        deg = degree if _type == 2 else -1 * degree
        arr[r1][c1] += deg
        arr[r2+1][c2+1] += deg
        deg *= -1
        arr[r2+1][c1] += deg
        arr[r1][c2+1] += deg
    
    for i in range(col_len):
        for j in range(1, row_len):
            arr[i][j] += arr[i][j-1]

    for i in range(1, col_len):
        for j in range(row_len):
            arr[i][j] += arr[i-1][j]

    for i in range(col_len):
        for j in range(row_len):
            if arr[i][j] + board[i][j] > 0:
                answer += 1
    
    return answer

if __name__ == '__main__':
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    solution(board, skill)