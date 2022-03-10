import heapq
import sys
input = sys.stdin.readline

def solution():
    answer = 'use the stairs'
    q = []
    heapq.heappush(q, (S, S, 0))
    dp = [False for _ in range(F+1)]
    while q:
        _,  current, cost =  heapq.heappop(q)
        if current == G:
            answer = cost
            break
    
        if not dp[current]:
            dp[current] = True
            up = current + U
            down = current - D
            if up <= F:
                heapq.heappush(q, (abs(G - up), up, cost + 1))
            if down >= 0:
                heapq.heappush(q, (abs(G - down), down, cost + 1))
    
    print(answer)

if __name__ == '__main__':
    global F, S, G, U, D
    F, S, G, U, D = map(int, input().strip().split())
    solution()
    