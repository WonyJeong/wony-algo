from math import ceil
import sys
input = sys.stdin.readline


def cal_fees(gap, fees):
    a,b,c,d = fees
    if gap <= a:
        return b
    print(ceil((gap - a)))
    return b + ceil((gap - a) / c) * d 

def solution(fees, records):
    answer = []
    dic = {}
    for record in records:
        time, car, tp = record.split(' ')
        hh, mm = time.split(':')
        _time = int(hh) * 60 + int(mm)
        if not car in dic:
            dic[car] = []

        dic[car].append(_time)
    
    for k in dic.keys():
        if len(dic[k]) % 2 != 0:
            dic[k].append(23*60 + 59)
        gap = 0
        for i in range(0, len(dic[k]), 2):
            gap += dic[k][i+1] - dic[k][i]
        
        dic[k] = cal_fees(gap, fees)
    keys = sorted(dic.keys())
    for key in keys:
        answer.append(dic[key])
    
    print(answer)

    return answer

if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    solution(fees, records)