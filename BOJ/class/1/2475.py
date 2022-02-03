import sys
input = sys.stdin.readline

def solution(_input):
    answer = 0
    for x in _input:
        answer += pow(int(x), 2)

    return answer % 10

if __name__ == '__main__':
    _input = input().strip().split()
    print(solution(_input))