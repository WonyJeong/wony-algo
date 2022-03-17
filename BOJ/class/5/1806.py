from math import inf
import sys
input = sys.stdin.readline

def solution():
    l = 0; r = 1;
    answer = inf; temp = arr[0]
    while l < r:
        if temp >= s:
            answer = min(answer, r - l)
            temp -= arr[l]; l += 1
        else:
            if r >= n: break
            temp += arr[r]; r = r + 1
    print(answer if answer != inf else 0)

if __name__ == '__main__':
    global n, s, arr
    n, s = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    solution()