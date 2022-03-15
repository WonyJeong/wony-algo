import sys
input = sys.stdin.readline

def solution(n):
    if n == 0: print(0)
    elif n >= 1023: print(-1)
    else:
        arr = [1,2,3,4,5,6,7,8,9]; arr2 = [1,2,3,4,5,6,7,8,9]
        vis = set()
        while True:
            temp = []; flag = False
            for v in arr2:
                if not v in vis:
                    flag = True; vis.add(v);
                    _str = str(v)
                    for i in range(9):
                        if int(_str[-1]) > i:
                            temp.append(int(_str + str(i)))
                        else:
                            break
            arr += temp; arr2 = temp
            if not flag: break
        print(arr[n-1])
        
if __name__ == '__main__':
    n = int(input().strip())
    solution(n)