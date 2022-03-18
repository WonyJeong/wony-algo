import sys
input = sys.stdin.readline

def solution(n, arr):
    print(arr)
    return

if __name__ == '__main__':
    n = int(input().strip())
    arr = sorted(list(map(int, input().strip().split())))
    solution(n, arr)