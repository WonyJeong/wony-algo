import sys
input = sys.stdin.readline


def multiply(a,b):
    f00 = (a[0] * b[0] + a[1] * b[2]) % 1000000
    f01 = (a[0] * b[1] + a[1] * b[3]) % 1000000
    f10 = (a[2] * b[0] + a[3] * b[2]) % 1000000
    f11 = (a[2] * b[1] + a[3] * b[3]) % 1000000
    return [f00, f01, f10,f11]

def fibo(n):
    if n == 1:
        return [1,1,1,0]

    if n % 2 == 0:
        _matrix = multiply(fibo(n//2), fibo(n//2))
    else:
        _matrix = multiply(fibo(n//2), fibo(n//2))
        _matrix = multiply(_matrix, fibo(1))
    
    return _matrix
    

        

def solution(n):
    _n = n % 1500000
    print(fibo(_n)[1])
    return

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)