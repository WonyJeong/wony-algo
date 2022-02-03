import sys



def solution(str):
    stack = []
    for i in range(len(str)):
        char = str[i]
        if char == '(' or char == '[':
            stack.append(char)

        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()            
            else:
                stack.append(char)
            
    print('yes') if len(stack) == 0 else print('no')

if __name__ == '__main__':
    arr = []
    while True:
        str = sys.stdin.readline()[:-1]
        if str == '.':
            print(str)
            break
        solution(str)