from collections import deque
from copy import deepcopy
from math import inf
import sys
input = sys.stdin.readline

cctv1_direction = [['left'], ['right'], ['up'], ['down']]
cctv2_direction = [['left', 'right'], ['up', 'down']]
cctv3_direction = [['up', 'right'], ['right', 'down'], ['down', 'left'], ['left', 'up']]
cctv4_direction = [['left', 'up', 'right'], ['down', 'up', 'right'],['left', 'down', 'right'],['left', 'up', 'down']]
cctv5_direction = [['left', 'up', 'right','down']]
cctv_directions = [cctv1_direction, cctv2_direction, cctv3_direction, cctv4_direction, cctv5_direction]

def cctv(_arr, i, j, directions):
    arr = deepcopy(_arr)
    for direction in directions:
        dx, dy = i, j
        while 0 <= dx < N and 0 <= dy < M:
            if arr[dx][dy] == 0:
                arr[dx][dy] = '#'

            if arr[dx][dy] == 6:
                break
            if direction == 'left':
                dy -= 1
            elif direction == 'right':
                dy += 1
            elif direction == 'up':
                dx -= 1
            elif direction == 'down':
                dx += 1
    return arr  
    
def solution(N, M, arr):
    answer = N * M
    q = deque([arr])
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] < 6:
                cctv_num =  arr[i][j]
                for _ in range(len(q)):
                    bot = q.popleft()
                    for directions in cctv_directions[cctv_num - 1]:
                        q.append(cctv(bot, i, j, directions))
    
    for matrix in q:
        temp = 0
        a = []
        for i in range(N):
            for j in range(M):        
                if matrix[i][j] == 0:
                    temp += 1
        answer = min(temp, answer)
    print(answer)
    return answer

                    
if __name__ == '__main__':
    global N, M
    N, M = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(N, M, arr)