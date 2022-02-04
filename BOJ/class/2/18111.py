import sys
input = sys.stdin.readline

def block(mp, h, block):
    time = 0
    _block = block
    arr = sorted(list(mp.keys()))
    for i in arr:
        height = i
        ct = mp[height]
        diff = abs(h - height) * ct
        if height < h:     
            _block -= diff
            time += diff
        
        if height > h:
            _block += diff
            time += 2 * diff
    return time if _block >= 0 else -1

def solution():
    N, M, B = map(int, input().strip().split())
    mp = {}
    _min = 300
    _max = -1
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        for i in range(M):
            if row[i] < _min : _min = row[i]
            if row[i] > _max : _max = row[i]
            if row[i] not in mp:
                mp[row[i]] = 0;
            mp[row[i]] += 1

    answer = 0, 0
    time = sys.maxsize
    for i in range(_min,_max+1):
         temp = block(mp, i, B)
         if temp != -1 and temp <= time:
             time = temp
             answer = [time, i]

    print(answer[0], answer[1])
    return answer

if __name__ == '__main__':
    solution()




