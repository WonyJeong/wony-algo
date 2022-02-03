import sys
input = sys.stdin.readline


def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                
    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__':
    N = int(input().strip())
    for _ in range(N):
        print(solution(input().strip()))




