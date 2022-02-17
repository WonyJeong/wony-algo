from math import ceil, sqrt
import sys
input = sys.stdin.readline

def translate(n, k):
    answer = ''
    temp = n
    while temp:
        quo = temp % k
        answer = str(quo) + answer 
        temp = temp // k
    return answer

def prime_checker(n):
    sq = sqrt(n)

    if n == 1: return True
    if n == 2: return False

    for i in range(2, ceil(sq + 1)):
        if n % i == 0 :
            return True
    return False


def solution(n, k):
    answer = 0
    kth_num = translate(n,k)
    for _num in kth_num.split('0'):
        if len(_num) > 0:
            if not prime_checker(int(_num)):
                answer += 1
    return answer
if __name__ == '__main__':
    n, k = 437674, 3
    n, k = 505, 1
    n, k = 211020101011, 10
    # n = int(input().strip())
    solution(n,k)