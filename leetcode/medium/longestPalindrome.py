import sys
input = sys.stdin.readline


def longestPalindrome(s):
    answer = ''
    for i in range(len(s)):
        sub_len = 0
        for j in range(i,len(s)):
            sub_len += 1
            if len(answer) > sub_len:
                continue

            if s[i:j+1] == s[i:j+1][::-1]:
                answer = s[i:j+1] if len(s[i:j+1]) > len(answer) else answer
    return answer

if __name__ == "__main__":
    s = "aacabdkacaa"
    print(longestPalindrome(s))          


