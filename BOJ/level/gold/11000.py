import heapq
import sys
input = sys.stdin.readline

def solution(n):
    hq = []; q = [];
    for _ in range(n):
        s, e = map(int, input().strip().split())
        heapq.heappush(hq, (s,e))
    while hq:
        x, y =  heapq.heappop(hq)
        if len(q) > 0:
            top = heapq.heappop(q)[0]
            if top > x:
                heapq.heappush(q, (top, top))
        heapq.heappush(q, (y, y))
    print(len(q))  

if __name__ == '__main__':
    n = int(input().strip())
    solution(n)
# 5
# 1 7
# 2 3
# 3 4
# 4 8
# 7 10