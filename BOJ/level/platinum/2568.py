from bisect import bisect_left
import sys
input = sys.stdin.readline

def solution(aTob, _bToa):
    bToa = _bToa
    arr = []
    lis = []
    keys =  sorted(aTob.keys())

    for key in keys:
        arr.append(aTob[key])
    lis.append(arr[0])
    index = [0]
    for i in range(1, len(keys)):
        if lis[-1] < arr[i]:
            lis.append(arr[i])
            index.append(len(lis) - 1)
        else:
            idx = bisect_left(lis, arr[i])
            lis[idx] = arr[i]
            index.append(idx)
    cursor = len(lis) - 1
    for i in range(N - 1, -1, -1):
        if index[i] == cursor:
            cursor -= 1
            bToa.pop(arr[i])
            
    print(len(keys) - len(lis))
    print('\n'.join(str(v) for v in sorted(bToa.values())))

if __name__ == '__main__':
    N = int(input().strip())
    aTob = {}
    bToa = {}
    for _ in range(N):
        A, B = map(int, input().strip().split())
        aTob[A] = B
        bToa[B] = A
    solution(aTob, bToa)
        