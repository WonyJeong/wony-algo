import sys
input = sys.stdin.readline

def solution(_input):
    if _input == '1 2 3 4 5 6 7 8':
        return 'ascending'
    elif _input == '8 7 6 5 4 3 2 1':
        return 'descending'
    else:
        return 'mixed'

if __name__ == '__main__':
    _input = input().strip()
    print(solution(_input))