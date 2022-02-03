import sys
input = sys.stdin.readline

from collections import deque


def solution(N):
    answer = 0
    q = deque([i+1 for i in range(N)])

    i = 0
    while len(q) != 1:
        if i % 2 == 0:
            q.popleft()
        else:
            bottom = q.popleft()
            q.append(bottom)
        i+=1    
    return q.popleft()
    

if __name__ == '__main__':
    N = int(input().strip())
    print(solution(N))

