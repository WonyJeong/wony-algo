import sys
input = sys.stdin.readline

def solution(n, histogram):
    result = 0; stack = []
    for i in range(n):
        while stack and histogram[stack[-1]] > histogram[i]:
            height = histogram[stack[-1]]
            stack.pop()
            width = i
            if stack:
                width = (i - stack[-1] - 1)
            result = max(result, width * height)
        stack.append(i)

    while stack:
        height = histogram[stack[-1]]
        stack.pop()
        width = n
        if stack:
            width = (n - stack[-1] - 1)
        result = max(result, width * height)
    print(result)

if __name__ == '__main__':
    while True:
        arr = list(map(int, input().strip().split()))
        histogram = arr[1:]
        if arr[0] == 0: break
        solution(arr[0], histogram)