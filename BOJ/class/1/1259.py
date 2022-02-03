import sys
input = sys.stdin.readline

def solution(s):
    print(s)
    return 'yes' if s == s[::-1] else 'no'

if __name__ == '__main__':
    while True:
        _input = input().strip()
        if _input != '0':
            print(solution(_input))
        else:
            break