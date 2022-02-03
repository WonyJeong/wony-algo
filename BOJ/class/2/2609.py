import sys
input = sys.stdin.readline

def gcd(a,b):
    _a, _b = [a,b] if b < a else [b,a]
    while _b > 0:
        temp = _b
        _b = _a % _b
        _a = temp
    return _a

def solution(a,b):
    _gcd = gcd(a,b)
    print(_gcd)
    print(int(a*b/_gcd))

if __name__ == '__main__':
    a, b= map(int, input().strip().split())
    solution(a,b)

