from math import inf
import sys
input = sys.stdin.readline


def soluion(n, dic):
    dist = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if i in dic:
            paths = dic[i]
            for path in paths:
                u,v,w = i, path[0], path[1]
                dist[u][v] = min(dist[u][v], w)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 기존 i -> j를,  i -> k -> j 로 돌아본다.
                if i == j:
                    continue
                ij = dist[i][j]
                ik = dist[i][k]
                kj = dist[k][j]

                dist[i][j] = min(ij, ik + kj)

    for i in range(n):
        print(' '.join(str(d) if d != inf else str(0) for d in dist[i]))

if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    dic = {}
    for _ in range(m):
        u,v,w = map(int, input().strip().split())
        if u-1 not in dic:
            dic[u-1] = set()
        dic[u-1].add((v-1,w))
    soluion(n,dic)
  