import sys
input = sys.stdin.readline

def solution(n, k, cmd):
    answer = ''
    linked_list = [[i-1, i+1, True] for i in range(n)]
    stack = []
    cursor = k
    for _cmd in cmd:
        _cmd = _cmd.split(' ')
        if _cmd[0] == 'U':
            d = int(_cmd[1])
            for _ in range(d):
                _next = linked_list[cursor][0]
                if _next < 0:
                    break
                cursor = _next
        elif _cmd[0] == 'D':
            d = int(_cmd[1])
            for _ in range(d):
                _next = linked_list[cursor][1]
                if _next > n-1:
                    break
                cursor = _next
        elif _cmd[0] == 'C':
            _prev, _next, _ = linked_list[cursor]
            stack.append(cursor)
            linked_list[cursor][2] = False
            if _prev > -1:
                linked_list[_prev][1] = _next
            if _next < n:
                linked_list[_next][0] = _prev
                cursor = _next
                continue
            cursor = _prev
        elif _cmd[0] == 'Z':
            if len(stack) >0:
                top = stack.pop()
                _prev, _next, _ = linked_list[top]
                linked_list[top][2] = True
                if _prev > 0:
                    linked_list[_prev][1] = top
                if _next < n:
                    linked_list[_next][0] = top
        print(linked_list)
    answer = ''.join('O' if cell[2] == True else 'X' for cell in linked_list)
    return answer

if __name__ == "__main__":
    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    print(solution(n,k,cmd)) # "OOOOXOOO"