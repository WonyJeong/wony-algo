import sys
input = sys.stdin.readline


def factorial(n):
    val = 1
    for i in range(1, n+1):
        val *= i
    return val

def solution(n,r):
    return int(factorial(n) / factorial(r) / factorial(n-r))

if __name__ == '__main__':
    n, c= map(int, input().strip().split())
    print(solution(n,c))




