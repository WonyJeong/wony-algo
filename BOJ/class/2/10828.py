import sys
input = sys.stdin.readline


def solution(N,cmds):
    stack = []

    for cmd in cmds:
        if cmd[0] == 'push':
            stack.append(int(cmd[1]))
        elif cmd[0] == 'top':
            print(stack[-1]) if len(stack) > 0 else print(-1)
        elif cmd[0] == 'pop':
            top = stack.pop() if len(stack) > 0 else -1
            print(top)
        elif cmd[0] == 'size':
            print(len(stack))
        elif cmd[0] == 'empty':
            print(1) if len(stack) == 0 else print(0)
        

if __name__ == '__main__':
    N = int(input().strip())
    cmd = []
    for _ in range(N):
        cmd.append(input().strip().split())
    solution(N,cmd)