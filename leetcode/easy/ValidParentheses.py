import sys

input = sys.stdin.readline



def isPair(left, right):
    return left == '(' and right == ')' or left == '[' and right == ']' or left == '{' and right == '}'


def isOpen(item):
    return item == '(' or item == '[' or item == '{'
        
def isValid(str):
    _str = list(str)
    stack = []
    for item in _str:
        _isOpen = isOpen(item)
        print(_isOpen)
        if(_isOpen):
            stack.append(item)
        else:
            if(len(stack) > 0):
                if(isPair(stack[-1], item)):
                    stack.pop()
                else:
                    return False
            else:
                return False

            
if __name__ == "__main__":
    print(isValid("()"))