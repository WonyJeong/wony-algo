from math import inf
import sys
from collections import deque
input = sys.stdin.readline

def solution(dic):
    arr = [inf for _ in range(101)]
    visited = [False for _ in range(101)]
    q = deque([1])
    dice = [1,2,3,4,5,6]
    arr[1] = 0
    while q:
        bot = q.popleft()
        if not visited[bot]:
            visited[bot] = True
            for d in dice:
                _next = bot + d
                if _next < 101:
                    if _next in dic:
                        _next = dic[_next]
                    if not visited[_next]:
                        arr[_next] = min(arr[bot] + 1, arr[_next])
                        q.append(_next)
    print(arr[100])


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    dic = {}
    for _ in range(N):
        _in, _out = map(int, input().strip().split())
        dic[_in] = _out
    for _ in range(M):
        _in, _out = map(int, input().strip().split())
        dic[_in] = _out

    solution(dic)
    
        
        