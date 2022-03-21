from bisect import bisect_left
import sys
input = sys.stdin.readline
def solution(n, arr):
    answer = [arr[0], arr[(n-1)//2], arr[n-1]]; fix = 0
    for i in range(n-2):
        fix = arr[i]; j = i + 1; k = n - 1
        while j < k:
            left = arr[j]; right = arr[k];
            total = fix + left + right            
            if abs(total) < abs(sum(answer)):
                answer = [fix, left, right]
                if total == 0:
                    return answer
            if total > 0: k -= 1
            else : j += 1
    return answer
if __name__ == '__main__':
    n = int(input().strip())
    arr = sorted(list(map(int, input().strip().split()))) 
    print(' '.join(str(i) for i in solution(n, arr)))