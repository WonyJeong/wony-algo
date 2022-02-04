import sys
import heapq

input = sys.stdin.readline

def solution():
    N = int(input().strip())
    q = []
    for _ in range(N):
        _input = int(input().strip())
        if _input == 0:
            if len(q) == 0:
                print(0)
            else:
                print(heapq.heappop(q))
        else:
            heapq.heappush(q, _input)
        


if __name__ == '__main__':
    solution()
    