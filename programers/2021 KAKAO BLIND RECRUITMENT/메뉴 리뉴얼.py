import sys
from itertools import combinations

input = sys.stdin.readline


def solution(orders, course):
    answer = []

    for cor in course:
        dic = {}
        for order in orders:
            order_ = sorted(list(order))
            for per in combinations(order_, cor):
                if not per in dic.keys():
                    dic[per] = set()
                    dic[per] = 0
                dic[per] += 1

        if len(dic.keys()) > 0:
            max_ = max(dic.values())
            if max_ > 1:
                for key in dic.keys():
                    if dic[key] == max_:
                        answer.append(''.join(key))
    answer2 = []
    for item in sorted(answer):
        temp = ""
        answer2.append(temp + item)
    return answer2