# import sys
# input = sys.stdin.readline

# def solution(n, m, arr):
#     nums = set()
#     # vis = [False for _ in range(100000001)]

#     # for i in range(len(vis)):
#     #     j = i*i; 
#     #     if j > 100000000: break
#     #     else: vis[j] = True

#     for i in range(n):
#         for j in range(m):
#             for cd in range(-1 * n, n):
#                 temp = ''
#                 for rd in range(-1 * m, m):

#                     if 0 <= i + cd < n and 0 <= j + rd  < m:
#                         temp += arr[i + cd][j + rd]
#                 nums.add(temp)
#                 nums.add(temp[::-1])



#     print(nums)
#     answer = -1
#     # for num in nums:
#     #     if num == '': continue
#     #     num = int(num)
#     #     print(num)
#     #     if vis[num]:
#     #         answer = max(answer, num)
#     # print(answer)

# if __name__ == '__main__':
#     n, m = map(int, input().strip().split())
#     arr = []
#     for _ in range(n):
#         arr.append(input().strip())
#     solution(n, m, arr)