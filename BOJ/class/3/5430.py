from curses.ascii import isdigit
import sys
input = sys.stdin.readline

def solution(p, n, arr):
    s, e = 0, len(arr) - 1
    ct = len(arr)
    is_reversed = False

    for _p in p:
        if _p == 'R':
            is_reversed = not is_reversed
        else:
            ct -= 1   
            if not is_reversed:
                s += 1
            else:
                e -= 1
                
            if ct < 0:
                return 'error'

    answer_arr = arr[s:e+1] if not is_reversed else list(reversed(arr[s:e+1]))

    return '[' + ','.join(str(v) for v in answer_arr) + ']'


def parseArray(arr):
    answer = []
    cursor = 0

    while cursor < len(arr):
        temp = ''

        while True:
            if isdigit(arr[cursor]):
                temp += arr[cursor]
                cursor += 1
            else:
                break

        if len(temp) > 0 : answer.append(int(temp))
        cursor += 1
    return answer

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        p = input().strip()
        n = int(input().strip())
        _arr = input().strip()
        arr = parseArray(_arr)
        print(solution(p,n,arr))
