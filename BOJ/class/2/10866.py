import sys
input = sys.stdin.readline

from collections import deque

def solution(N,cmds):
    q = deque([])

    for cmd in cmds:
        if cmd[0] == 'push_front':
            q.appendleft(int(cmd[1]))
        elif cmd[0] == 'push_back':
            q.append(int(cmd[1]))
        elif cmd[0] == 'front':
            print(q[0]) if len(q) > 0 else print(-1)
        elif cmd[0] == 'back':
            print(q[-1]) if len(q) > 0 else print(-1)
        elif cmd[0] == 'pop_front':
            bottom = q.popleft() if len(q) > 0 else -1
            print(bottom)
        elif cmd[0] == 'pop_back':
            top = q.pop() if len(q) > 0 else -1
            print(top)
        elif cmd[0] == 'size':
            print(len(q))
        elif cmd[0] == 'empty':
            print(1) if len(q) == 0 else print(0)
        

if __name__ == '__main__':
    N = int(input().strip())
    cmd = []
    for _ in range(N):
        cmd.append(input().strip().split())
    solution(N,cmd)