import sys
input = sys.stdin.readline

def solution(id_list, report, k):
    answer = []
    dic = {}
    count_dic = {}
    for _id in id_list:
        dic[_id] = set()
        count_dic[_id] = set()

    for rep in report:
        u, v = rep.split(' ')
        dic[u].add(v)
        count_dic[v].add(u)
    
    for u in dic:
        temp = 0
        for v in dic[u]:
            if len(count_dic[v]) >= k:
                temp += 1
        answer.append(temp)

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    solution(id_list, report, k)

    