import sys
input = sys.stdin.readline
# https://www.acmicpc.net/blog/view/12
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
    n = int(input().strip())
    histogram = []
    for _ in range(n):
        histogram.append(int(input().strip()))
    solution(n, histogram)