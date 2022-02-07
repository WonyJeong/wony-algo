import sys
input = sys.stdin.readline


def solution(l):
    answer = 1
    for ct in l:
        answer *= (ct+1)
    print(answer-1)
        
if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        dic = {}
        for _ in range(n):
            wear, wear_type = map(str, input().strip().split())
            if not wear_type in dic:
                dic[wear_type] = 0
            dic[wear_type] += 1
        solution(list(dic.values()))
            