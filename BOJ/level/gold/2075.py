import heapq
import sys
input = sys.stdin.readline

def solution(N):
    q = []
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        for r in row:
            heapq.heappush(q, (r, r))
            if len(q) > N:
                heapq.heappop(q)
    print(heapq.heappop(q)[0])

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)