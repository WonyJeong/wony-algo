import sys
import heapq

input = sys.stdin.readline

def get_value(heap, dic):
    _heap = heap
    while True:
        if len(_heap) == 0:
            return 'x'
        top = heapq.heappop(_heap)[1]
        if top in dic and dic[top] > 0:
            return top

def solution():
    K = int(input().strip())
    min_heap, max_heap  = [], []
    dic = {}
    
    for _ in range(K):
        cmd, n = map(str, input().strip().split())
        n = int(n)
        if cmd == 'I':
            heapq.heappush(min_heap, (n,n))
            heapq.heappush(max_heap, (-n,n))
            if not n in dic:
                dic[n] = 0
            dic[n] += 1
        else:
            if n == -1: # 최소값 pop                
                while True:
                    if len(min_heap) == 0: break
                    _min = heapq.heappop(min_heap)[1]
                    if _min in dic and dic[_min] > 0:
                        dic[_min] -= 1
                        break

            else:       # 최대값 pop
                while True:
                    if len(max_heap) == 0 : break
                    _max = heapq.heappop(max_heap)[1]
                    if _max in dic and dic[_max] > 0:
                        dic[_max] -= 1
                        break

    _min = get_value(min_heap, dic)
    _max = get_value(max_heap, dic)

    print(_max, _min) if _min != 'x' else print('EMPTY')
    
if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        solution()