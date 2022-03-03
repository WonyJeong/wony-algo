import sys
input = sys.stdin.readline

def solution(lottos, win_nums):
    answer = []
    match_count = 0
    deleted_lotto = 0 
    for lotto in lottos:
        if lotto == 0:
            deleted_lotto += 1
            continue
        for i in range(6):
            if win_nums[i] == lotto: match_count += 1
    _max = 7 - (match_count + deleted_lotto)
    _min = 7 - (match_count)
    return [_max if _max < 7 else 6, _min if _min < 7 else 6]
    
if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    solution(lottos, win_nums)