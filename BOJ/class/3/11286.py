import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    q = []
    for _ in range(N):
        temp = int(input().strip())
        if temp != 0:
            heapq.heappush(q, (abs(temp), temp))
        else:
            if len(q) != 0:
                print(heapq.heappop(q)[1])
            else:
                print(0)