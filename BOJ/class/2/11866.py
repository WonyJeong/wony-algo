import sys
input = sys.stdin.readline

from collections import deque

def solution(N,K):
    answer = []
    q = deque([i+1 for i in range(N)])

    i = 0
    while len(answer) != N:
        i += 1
        if i == K:
            bottom = q.popleft()
            answer.append(bottom)
            i = 0
        else:
            bottom = q.popleft()
            q.append(bottom)

    print('<' + ', '.join(str(i) for i in answer)+'>')
if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    solution(N,K)