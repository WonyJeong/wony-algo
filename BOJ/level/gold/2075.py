import heapq
import sys
input = sys.stdin.readline

def solution(N, arr):
    q = []
    for i in range(N):
        for j in range(N):
            k = arr[i][j]
            if len(q) > N*N - N:
                heapq.heappop(q)
            heapq.heappush(q, (k, k))
        
    print(q, len(q))

if __name__ == '__main__':
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(N, arr)