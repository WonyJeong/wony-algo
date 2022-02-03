import sys
input = sys.stdin.readline

def isPalindrome(num):
    num = str(num)
    return True if num == num[::-1] else False


if __name__ == "__main__":
    print(isPalindrome(1201))