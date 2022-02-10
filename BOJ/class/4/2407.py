from math import factorial
import sys
input = sys.stdin.readline

def solution(n,m):
    return factorial(n) // (factorial(n-m) * factorial(m))

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    print(solution(n,m))