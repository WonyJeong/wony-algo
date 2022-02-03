import sys
input = sys.stdin.readline


def translate(s):
    dic = {
            'zero' :'0',
            'one' :'1',
            'two' :'2',
            'three' :'3',
            'four' :'4',
            'five' :'5',
            'six' :'6',
            'seven' :'7',
            'eight' :'8',
            'nine' :'9',
        }
    if s in dic:
        return dic[s]
    else:
        return ''

def solution(s):
    answer = ''    
    _s = s
    while _s != '':
        if _s[0].isdigit():
            answer += _s[0]
            _s = _s[1:]
        else:
            if translate(_s[0:3]) != '':
                idx = 3
            elif translate(_s[0:4]) != '':
                idx = 4
            else:
                idx = 5

            answer += translate(_s[0:idx])
            _s = _s[idx:]
            if _s == '':
                break

    return answer


if __name__ == "__main__":
    print(solution('one4seveneight'))
    print(solution('23four5six7'))
    print(solution('2three45sixseven'))
    print(solution('123'))