import sys
input = sys.stdin.readline


def solution(_arr, q):
    arr = _arr

    for i in range(len(arr)):
        for j in range(1, len(arr)):
            arr[i][j] += arr[i][j-1]
    for i in range(1, len(arr)):
        for j in range( len(arr)):
            arr[i][j] += arr[i-1][j]
    for row in q:
        x1, y1, x2, y2 = row
        temp = 0
        temp += arr[x2][y2]

        if x1 > 0 and y1 > 0 :
            temp -= (arr[x1-1][y2] + arr[x2][y1-1]) - arr[x1-1][y1-1]
        
        if x1 > 0 and y1 == 0:
            temp -= arr[x1-1][y2]
        
        if x1 == 0 and y1 > 0:
            temp -= arr[x2][y1-1]
        

        print(temp)

if __name__ == '__main__':
    N, M = map(int , input().strip().split())
    arr = []
    q = []
    for _ in range(N):
        arr.append(list(map(int , input().strip().split())))
    for _ in range(M):
        x1, y1, x2, y2 = list(map(int , input().strip().split()))
        q.append([x1-1,y1-1,x2-1,y2-1])
    solution(arr,q)
