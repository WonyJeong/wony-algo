import sys
input = sys.stdin.readline

def solution(n, s, arr):
    answer = 0
    for i in range(1, 1 << n):
        total = 0
        for j in range(n):
            total += arr[j] if (i & 1 << j) else 0
        if total == s: answer += 1
    print(answer)

if __name__ == '__main__':
    n, s = map(int, input().strip().split())
    arr = list(map(int, input().strip().split())) 
    solution(n, s, arr)