from collections import deque
import sys
input = sys.stdin.readline


def command_d(n):
    return 2 * n if 2 * n < 10000 else (2 * n) % 10000

def command_s(n):
    return n-1 if n > 0 else 9999

def command_l(n):
    f = n % 1000
    b = n // 1000
    return f * 10 + b

def command_r(n):
    f = n % 10
    b = n // 10
    return f * 1000 + b

def bfs(A,B):
    q = deque([[A, '']])
    visited = set()
    while q:
        value, cmd = q.popleft()
        if value == B:
            return cmd
        if not value in visited:
            visited.add(value)
            d_value = command_d(value)
            if d_value not in visited:
                q.append([d_value, cmd + 'D'])
            s_value = command_s(value)
            if s_value not in visited:
                q.append([s_value, cmd + 'S'])
            l_value = command_l(value)
            if l_value not in visited:
                q.append([l_value, cmd + 'L'])
            r_value = command_r(value)
            if r_value not in visited:
                q.append([r_value, cmd + 'R'])

def solution(A,B):
    answer = bfs(A,B)
    print(answer)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        A, B = map(int, input().strip().split())
        solution(A,B)
