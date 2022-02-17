from collections import deque
import sys
input = sys.stdin.readline

def dfs(dic):
    stack = ['A']
    visited = {}
    answer = ''
    while stack:
        top = stack.pop()

        if not top in visited:
            visited[top] = False 

        if not visited[top]:
            visited[top] = True
            answer += top
            for i in range(len(dic[top])):
                stack.append(dic[top][len(dic[top])-i-1])
    
    return answer

def bfs(dic):
    q = deque(['A'])
    visited = {}
    answer = ''
    while q:
        bot = q.popleft()
        if not bot in visited:
            visited[bot] = False 
        if not visited[bot]:
            visited[bot] = True
            # answer += bot
            flag = False
            for i in range(len(dic[bot])):
                if not flag:
                    q.append(dic[bot][i])
                    flag = True
                else:
                    q.appendleft(dic[bot][i])
                # q.append(dic[bot][len(dic[bot])-i-1])
    print(answer)
    return answer


def solution(dic):
    answer1 = dfs(dic)
    answer2 = bfs(dic)

if __name__ == '__main__':
    N = int(input().strip())
    dic = {}
    for _ in range(N):
        x, y, z = map(str, input().strip().split())
        if x not in dic:
            dic[x] = []
        if y != '.' : dic[x].append(y)
        if z != '.' : dic[x].append(z)
    solution(dic)

        