import sys
input = sys.stdin.readline



def solution(a,b,c):
    arr = sorted([a,b,c])
    return 'right' if pow(arr[0],2) + pow(arr[1],2) == pow(arr[2],2) else 'wrong'

if __name__ == '__main__':
    while True:
        a, b, c= map(int, input().strip().split())
        if a+b+c == 0:
            break
        print(solution(a,b,c))

