from math import  floor
import sys
input = sys.stdin.readline

def dfs(start, amount):
    stack = [(start, amount * 100)]
    while stack:
        current, amount = stack.pop()
        if amount < 10:
            cost[current] += amount
            return
        else:
            if current == '-':
                cost[current] += amount
            for next in dic[current]:
                next_cost = floor(amount * 0.1)
                current_cost = amount - next_cost
                cost[current] += current_cost
                stack.append((next, next_cost))

def solution(enroll, referral, seller, amount):
    global dic, cost
    answer = []
    dic = {}
    cost = {}
    cost['-'] = 0
    dic['-'] = set()
    for i in range(len(enroll)):
        enr = enroll[i]
        ref = referral[i]
        dic[enr] = set()
        cost[enr] = 0
        dic[enr].add(ref)
    for i in range(len(seller)):
        dfs(seller[i], amount[i])
    
    for i in range(len(enroll)):
        answer.append(int(cost[enroll[i]]))
    
    return answer

if __name__ == '__main__':
    enroll =["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral =["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller =["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    solution(enroll, referral, seller, amount)
    