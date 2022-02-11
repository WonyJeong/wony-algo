# from collections import deque
# import sys
# input = sys.stdin.readline

# # 가로 : 0
# # 세로 : 1
# # 대각선 : 2

# def dfs(T, arr):
#     answer = 0
#     stack = [[0,1,0, '']]
#     _set = set()
#     temp = ''
#     while stack:
#         x, y, z, temp = stack.pop()

#         if x == T-1 and y == T-1:
#             answer += 1
#             print(temp)
#             continue
#         # # if (x,y,z in _set):
#         #     # print()
#         # # else:
#         # if (x,y,z) not in _set:
#         _set.add((x,y,z))    
#         nhx, nhy = x, y + 1       # 다음 세로 배치
#         nvx, nvy = x + 1, y       # 다음 가로 배치
#         ndx, ndy = x + 1, y + 1   # 다음 대각 배치
#         if z != 1 and (0<= nhx < T) and (0<= nhy < T)  and arr[nhx][nhy] == 0:
#             stack.append((nhx, nhy, 0, temp + '→ ,'))
#         if z != 0 and (0<= nvx < T) and (0<= nvy < T)  and arr[nvx][nvy] == 0:
#             stack.append((nvx, nvy, 1 , temp + '↓ ,'))
#         if (0 < ndx < T) and (0 < ndy < T)  and arr[ndx][ndy] == 0 and arr[ndx-1][ndy] == 0 and arr[ndx][ndy-1] == 0:
#             stack.append((ndx, ndy, 2 , temp + '↘ ,'))

#     return answer


# def solution(T, arr):
#     temp = [[set() for _ in range(T)] for _ in range(T)]
#     answer = [[0 for _ in range(T)] for _ in range(T)]




# if __name__ == '__main__':
#     T = int(input().strip())
#     arr = []
#     for _ in range(T):
#         arr.append(list(map(int, input().strip().split())))
#     print(solution(T, arr))

from collections import deque
import sys
input = sys.stdin.readline

# 가로 : 0
# 세로 : 1
# 대각선 : 2

def dfs(T, arr):
    answer = 0
    stack = [[0,1,0]]
    while stack:
        x, y, z = stack.pop()
        if x == T-1 and y == T-1:
            answer += 1
            continue
        nhx, nhy = x, y + 1       # 다음 세로 배치
        nvx, nvy = x + 1, y       # 다음 가로 배치
        ndx, ndy = x + 1, y + 1   # 다음 대각 배치
        if z != 1 and (0<= nhx < T) and (0<= nhy < T)  and arr[nhx][nhy] == 0:
            stack.append((nhx, nhy, 0))
        if z != 0 and (0<= nvx < T) and (0<= nvy < T)  and arr[nvx][nvy] == 0:
            stack.append((nvx, nvy, 1 ))
        if (0 < ndx < T) and (0 < ndy < T)  and arr[ndx][ndy] == 0 and arr[ndx-1][ndy] == 0 and arr[ndx][ndy-1] == 0:
            stack.append((ndx, ndy, 2 ))

    return answer

if __name__ == '__main__':
    T = int(input().strip())
    arr = []
    for _ in range(T):
        arr.append(list(map(int, input().strip().split())))
    print(dfs(T, arr))