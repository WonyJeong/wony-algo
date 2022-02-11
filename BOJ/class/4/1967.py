import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    for _ in range(n-1):
        u, v, w = map(int, input().strip().split())
        if not u in dic:
            dic[u] = set()
        if not v in dic:
            dic[v] = set()
        dic[u].add(v,w)
        dic[v].add(u,w)