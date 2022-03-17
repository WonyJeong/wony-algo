from cmath import inf
import sys
input = sys.stdin.readline

def solution(n, arr):
    l = 0; r = n-1; temp = [inf, l, r]
    while l < r:
        left = arr[l]; right = arr[r]
        if temp[0] >= abs(right + left): temp = [abs(right + left), l, r]
        if left + right == 0: break
        if left + right > 0: r -= 1
        else: l += 1
    print(arr[temp[1]], arr[temp[2]])

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(n, arr)