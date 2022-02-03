import sys
input = sys.stdin.readline

def solution(N, locations):
    _keys = sorted(list(set(locations)))
    dic = {}
    for i in range(len(_keys)):
        dic[_keys[i]] = i
    
    return ' '.join(str(dic[i]) for i in locations)
    
    

if __name__ == '__main__':
    N = int(input())
    locations = list(map(int, input().strip().split()))
    print(solution(N, locations))
    