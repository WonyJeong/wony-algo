import sys
input = sys.stdin.readline

def solution(N,arr):
    answer = abs(100 - N)
    button = [True for _ in range(10)]
    for i in arr:
        button[i] = False
    for i in range(1000001):
        flag = True
        for char in str(i):
            if not button[int(char)]:
                flag = False
                break
        if flag: 
            answer = min(answer, abs(N - i) + len(str(i)))
    print(answer)

if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())
    arr = []
    for _ in range(M):
        arr = list(map(int, input().strip().split()))
        break
    solution(N,arr)