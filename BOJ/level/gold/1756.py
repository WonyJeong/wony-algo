import sys
input = sys.stdin.readline

def soliution(oven, pizza):
    ct = 0
    limit = len(oven) - 1
    arr = [0 for _ in range(len(oven))]
    arr[0] = oven[0]
    for i in range(1, len(arr)):
        arr[i] = min(oven[i], arr[i-1])

    for r in pizza:
        while limit > -1:
            if r <= arr[limit]:
                limit -= 1
                ct = ct + 1
                break
            limit -= 1

    print(limit + 2 if ct == len(pizza) else 0)    

if __name__ == '__main__':
    D, N = map(int, input().strip().split())
    oven = list(map(int, input().strip().split()))
    pizza = list(map(int, input().strip().split()))
    soliution(oven, pizza)