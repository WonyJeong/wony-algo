import sys
input = sys.stdin.readline

# type : 0 - 기둥, 1 - 보

def pillarCheck(arr,x,y):
    # 바닥 위에 있거나, 다른 기둥 위에 있음
    if y == 0 or arr[x][y-1][0] == 0:
        return True

    # 보의 한쪽 끝에 설치 되어 있는 경우
    if arr[x-1][y][1] == 1 and arr[x][y][1] != 1:
        return True
    
    return False

def paperCheck(arr,x,y):
    #보의 한쪽 끝 부분이 기둥 위에 있음
    if y == 0 or arr[x][y-1][0] == 0:
        return True
    if x < n and y > 0 and arr[x+1][y-1][0] == 0:
        return True

    # 양쪽 끝 부분이 다른 보와 동시에 연결되어있음
    if x > 0 and x < n and arr[x-1][y][1] == 1 and arr[x+1][y][1] == 1:
        return True

    return False

def deletePillar(x,y,a,arr):
    _arr = arr
    _arr[x][y][a] = -1

    return False

def deletePaper(x,y,a,arr):
    _arr = arr
    _arr[x][y][a] = -1

    if (x > 0 and _arr[x-1][y][1] == 1) and (x < n and _arr[x+1][y][1] == 1):
        return True
    
    if (x < n and arr[x+1][y][0] == 0):
        return False

    return True


def solution(n, build_frame):
    answer = [[]]
    #[기둥, 보]
    arr = [[[-1,-1] for _ in range(n)] for _ in range(n)]
    for action in build_frame:
        x,y,a,b = action
        if b == 0: # 삭제
            
            print()
        else: # 설치
            flag = paperCheck(arr,x,y) if a == 0 else paperCheck(arr,x,y)
            if flag:
                arr[x][y][a] = a

    print(arr) 

    return answer

if __name__ == "__main__":
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

    solution(n, build_frame)

