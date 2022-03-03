from math import inf
import sys
input = sys.stdin.readline

def matrix_rotate(matrix, x1, y1, x2, y2):
    new_matrix = [[-1  for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    _min = inf
    # top
    for i in range(y1, y2+1):
        if y1 == i:
            new_matrix[x1][y1] = matrix[x1+1][y1]
        else:
            new_matrix[x1][i] = matrix[x1][i-1]
    # right
    for i in range(x1+1, x2):
        new_matrix[i][y2] = matrix[i-1][y2]
    # bottom
    for i in range(y1, y2+1):
        if y2 == i:
            new_matrix[x2][y2] = matrix[x2-1][y2]
        else:
            new_matrix[x2][i] = matrix[x2][i+1]
    # left
    for i in range(x1+1, x2):
        new_matrix[i][y1] = matrix[i+1][y1]
    
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            if new_matrix[i][j] == -1:
                new_matrix[i][j] = matrix[i][j]
            else:
                _min = min(_min, new_matrix[i][j])

    return new_matrix, _min

def solution(rows, columns, queries):
    answer = []
    matrix = [[((i) * columns + j + 1)  for j in range(columns)] for i in range(rows)]

    for x1,x2,y1,y2 in queries:
        matrix, _min = matrix_rotate(matrix, x1-1,x2-1,y1-1,y2-1)
        answer.append(_min)
    
    return answer

if __name__ == '__main__':
    rows = 6
    columns = 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    solution(rows, columns, queries)

    