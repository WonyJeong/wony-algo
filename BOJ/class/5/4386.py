import heapq
import math
import sys
input = sys.stdin.readline

def get_dist(a, b):
    x1, y1 = a; x2, y2 = b;
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def solution(n, arr):
    dic = {}
    for i in range(n):
        dic[i] = []
        for j in range(n):
            if i == j: continue
            dic[i].append((get_dist(arr[i], arr[j]), j))
    q = []; vis = set(); vis.add(0); ct = 1
    answer = 0
    for w, v in dic[0]: heapq.heappush(q, (w,v))
    while ct != n:
        while q:
            w, v = heapq.heappop(q)
            if not v in vis: break
        vis.add(v); ct += 1
        answer += w
        for _w, _v in dic[v]: heapq.heappush(q, (_w,_v))
    print(answer)
if __name__ == '__main__':
    n = int(input().strip())
    arr = [list(map(float, input().strip().split())) for _ in range(n)]
    solution(n, arr)