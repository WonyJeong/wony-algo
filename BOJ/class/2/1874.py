import sys
input = sys.stdin.readline


def solution(N, stack):
    answer = []
    arr = []
    i, cursor = 1, 0
    temp = []
    while i <= N:
        current = stack[cursor]
        top = arr[-1] if len(arr) > 0 else -1
        if current == top:
            answer.append('-')
            bot = arr.pop()
            temp.append(bot)
            cursor += 1
        else:
            arr.append(i)
            answer.append('+')
            i += 1
    
    answer += ['-'] * len(arr) 

    print('\n'.join(cmd for cmd in answer)) if temp + arr[::-1] == stack else print('No')
            
if __name__ == '__main__':
    N = int(input().strip())
    stack = []
    for _ in range(N):
        stack.append(int(input().strip()))
    solution(N, stack)