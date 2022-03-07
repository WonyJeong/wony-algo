from bisect import bisect_left
import sys
input = sys.stdin.readline

def solution(dic):
    arr = []
    dp = []
    keys =  sorted(dic.keys())
    for key in keys:
        arr.append(dic[key])
    dp.append(arr[0])
    for i in range(len(keys)):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            idx = bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    print(len(keys) - len(dp))

if __name__ == '__main__':
    N = int(input().strip())
    dic = {}
    for _ in range(N):
        A, B = map(int, input().strip().split())
        dic[A] = B
    solution(dic)
        