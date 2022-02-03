import sys
input = sys.stdin.readline


def lengthOfLongestSubstring(s):
    answer = 0
    for i in range(len(s)):
        temp = 0
        dic = {}
        for j in range(i,len(s)):
            if not s[j] in dic:
                temp += 1
                dic[s[j]] = ''
                answer = max(answer, temp)
            else:
                i = j-1
                break

    return answer

if __name__ == "__main__":
    s = '1234 1234 5678'
    print(lengthOfLongestSubstring(s))