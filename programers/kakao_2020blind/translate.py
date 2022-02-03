import sys

input = sys.stdin.readline

def isCorrect(s):
    stack = []
    for i in range(len(s)):
        char = s[i]

        if len(stack) == 0:
            stack.append(char)
            continue

        if stack[-1] == '(' and char == ')':
            stack.pop()
            continue

        stack.append(char)

    return True if len(stack) == 0 else False

def divide(p):
    left = right = 0
    temp = 0

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            break
    
    return p[0:2*left], p[2*left:]

def recirsive(s):
    result = ''
    result = '('
    for i in range(len(_u)):
        if _u[i] == '(':
            result += ')'
        else:
            result += '('
    result += ')'


    return result

def edit(u,v):
    result = '('
    result += v
    result += ')'
    _u = u[1:len(u)-1]
    

    return result

def solution(p):
    answer = ''
    _p = p

    while True:
        if _p == '':
            return answer

        u, v = divide(_p)
        u_state = isCorrect(u)

        if(u_state):
            answer += u
            _p = v

        else:
            answer += edit(u,v)
            break
        
    return answer


if __name__ == "__main__":
    # p = '(()())()'
    # p = ')('
    p = ')()()()('
    print(solution(p))