import sys

input = sys.stdin.readline

def compressString(arr):
    compress = ""
    cursor = 1
    _part = arr[0]
    _prefix = 1

    while cursor <= len(arr):
        if cursor < len(arr) and arr[cursor] == _part:
            _prefix += 1

        else:
            _num = str(_prefix) if _prefix > 1 else ""
            compress += _num + _part
            _prefix = 1

            if cursor != len(arr):
                _part = arr[cursor]


        cursor += 1

    return compress


def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        arr = []
        for j in range(0,len(s),i):
            arr.append(s[j:j+i])
        print('-------------------', arr, '-------------------')
        compress = compressString(arr)
        print(compress,answer)
        if len(compress) < len(s):
            answer = len(compress)
    print(answer)
    return answer

if __name__ == "__main__":
    # s = 'aabbaccc'
    # solution(s)
    # s = 'ababcdcdababcdcd'
    # solution(s)
    # s = 'abcabcdede'
    # solution(s)
    # s = 'abcabcabcabcdededededede'
    # solution(s)
    # s = 'xababcdcdababcdcd'
    # solution(s)
    s = 'aaaaa'
    solution(s)