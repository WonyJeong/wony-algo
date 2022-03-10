from collections import deque

def compare_max_total_array(arr1, arr2):
    for i in range(11):
        cursor = 10 - i
        if 0 <= arr1[cursor] < arr2[cursor]:
            return arr2
        if 0 <= arr2[cursor] < arr1[cursor]:
            return arr1
    return arr1

def cal_total(info, score):
    r_point = 0
    a_point = 0
    for i in range(11):
        if 0 <= info[i] < score[i]:
            r_point += 10 - i
        elif 0 <= score[i] < info[i] :
            a_point += 10 - i
    return r_point - a_point

def bfs(n, info):
    total_score = 0
    answer = []
    q = deque([[0, n, [0 for _ in range(11)]]])
    while q:
        cursor, res, scores = q.popleft()
        if cursor == 11:
            if res > 0:
                scores[10] += res
            score = cal_total(info, scores)
            if total_score < score:
                answer = scores
                total_score = score
            if total_score == score and answer != []:
                answer = compare_max_total_array(answer, scores)
            continue

        q.append([cursor + 1, res, scores])
        if res - info[cursor] > 0:
            temp_scores = scores[:]
            temp_scores[cursor] = info[cursor] + 1
            q.append([cursor + 1, res - (info[cursor] + 1), temp_scores])
    return answer

def solution(n, info):
    scores = bfs(n, info)
    return scores if scores != [] else [-1]