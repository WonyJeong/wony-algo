import sys
input = sys.stdin.readline

# ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]

dx_a = [-2,0,2,0]
dy_a = [0,2,0,-2]

dx_b = [-1,-1,1,1]
dy_b = [-1,1,1,-1]

dx_c = [-1,0,1,0]
dy_c = [0,1,0,-1]


def checkKeepDistance(arr, i,j):
    # Case A 
    for k in range(4):
        dx = i + dx_a[k]
        dy = j + dy_a[k]
        if(dx >= 0 and dy >= 0 and dx<5 and dy<5):
            if(arr[dx][dy] == 'P'):
                if arr[int((dx + i)/2)][int((dy + j)/2)] != 'X':
                    return False
    # Case B
    for k in range(4):
        dx = i + dx_b[k]
        dy = j + dy_b[k]
        if(dx >= 0 and dy >= 0 and dx<5 and dy<5):
            if(arr[dx][dy] == 'P'):
                if not (arr[dx][j] == 'X' and arr[i][dy] == 'X'):
                    return False
    # Case C
    for k in range(4):
        dx = i + dx_c[k]
        dy = j + dy_c[k]
        if(dx >= 0 and dy >= 0 and dx<5 and dy<5):
            if(arr[dx][dy] == 'P'):
                return False

    return True

def checkPlace(place):
    arr = []
    for row in place:
        arr.append(list(row))

    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                if not checkKeepDistance(arr,i,j):
                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(checkPlace(place))
    print(answer)
    return answer

if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    solution(places) # [1, 0, 1, 1, 1]