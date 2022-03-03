import sys
input = sys.stdin.readline

def solution(nums):
    _len = max(nums)
    arr = [1 for _ in range(_len+1)]
    for i in range(2, _len+1):
        for j in range(1, _len+1):
            if i * j > _len:
                break
            arr[i * j] += i
    for i in range(2, _len+1):
        arr[i] += arr[i-1]
    for ans in nums:
        print(arr[ans])
if __name__ == '__main__':
    T = int(input().strip())
    nums = []
    for _ in range(T):
        nums.append(int(input().strip()))
    solution(nums)