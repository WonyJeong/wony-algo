import sys
from bisect import bisect_left

input = sys.stdin.readline


def solution(N, arr):
    answer = []
    lis = [arr[0]]
    for i in range(1, N):
        if lis[-1] < arr[i]:
            lis.append(arr[i])
        else:
            idx = bisect_left(lis, arr[i])
            lis[idx] = arr[i]
    
    print(N - len(lis))

if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(int(input().strip()))
    solution(N, arr)
