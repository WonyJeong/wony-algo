from collections import deque
import sys
input = sys.stdin.readline

def solution(N, arr):
    answer = [0 for _ in range(N)]
    q = deque([(arr[-1], N-1)])
    stack = [(arr[0], 0)]

    for i in range(1, N):
        while stack:
            h, idx = stack[-1]
            if h <= arr[i]:
                stack.pop()
            else:
                answer[i] = idx + 1
                break
        stack.append((arr[i], i))
    print(' '.join(str(v) for v in answer))
        

if __name__ == '__main__':
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(N, arr)
