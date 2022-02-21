import sys
input = sys.stdin.readline

def solution(str, boom):
    stack = []
    boom_len = len(boom)
    for i in range(len(str)):
        stack.append(str[i])
        last_char = stack[-1]
        if last_char == boom[-1] and ''.join(stack[-boom_len:]) == boom:
            del stack[-boom_len:]
    print(''.join(stack)) if len(stack) > 0 else print('FRULA')

if __name__ == '__main__':
    str = input().strip()
    boom = input().strip()
    solution(str, boom)