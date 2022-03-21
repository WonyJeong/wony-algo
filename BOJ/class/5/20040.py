from re import A
import sys
input = sys.stdin.readline

def find(u):
    if parent[u] != u: parent[u] = find(parent[u])
    return parent[u]

def union(u,v):
    if u < v: parent[v] = u
    else: parent[u] = v

if __name__ == '__main__':
    global parent
    n, m = map(int,input().strip().split())
    parent = [i for i in range(n)]
    answer = 0
    for i in range(m):
        u, v = map(int,input().strip().split())
        u = find(u); v = find(v)
        if u == v:
            answer = i + 1
            break
        else: union(u,v)
    print(answer)
        
