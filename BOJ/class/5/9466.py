import sys
input = sys.stdin.readline

def dfs(start, arr):
    stack = [start]
    visited = [False for _ in range(len(arr))]
    vis = set()
    while stack:
        node = stack.pop()
        
        if node not in vis:
            vis.add(node)
            next = arr[node]

 
  
   


def solution(n, arr):
    for i in range(n):
        dfs(i, arr)
    return

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        solution(int(input().strip()), list(map(int, input().strip().split())))