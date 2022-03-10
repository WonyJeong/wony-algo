from collections import deque
import sys
input = sys.stdin.readline

def solution(N, L, arr):
    q, idx = deque([]), 0
    for item in arr:
        while True:
            if len(q) > 0 and q[-1][0] > item: q.pop()
            else : break;
        if len(q) > 0 and q[0][1] == idx - L: q.popleft()
        q.append((item, idx))
        print(q[0][0], end=' ')
        idx += 1
if __name__ == '__main__':
    N, L = map(int, input().strip().split())
    arr = map(int, input().strip().split())
    solution(N, L, arr)