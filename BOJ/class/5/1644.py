import math
import sys
input = sys.stdin.readline
def solution(n):
    primes = [True for _ in range(4000001)];
    primes[0] = False; primes[1] = False;
    arr = [0]
    for i in range(2, 4000001):
        if primes[i]:
            arr.append(arr[-1]+i)
            for j in range(i+i, 4000001, i):
                if j > 4000000: break
                primes[j] = False
    total = 2; l = 0; r = 1; answer = 0;
    while l < r:
        if n == total:
            answer += 1
        if total < n:
            r += 1
            if r == len(arr): break
        else: l += 1
        total = arr[r] - arr[l]
    print(answer)
if __name__ == '__main__':
    solution(int(input().strip()))