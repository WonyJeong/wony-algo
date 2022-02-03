class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1, l2):
        answer = []
        # l1 = ''.join(str(_) for _ in l1)[::-1]
        # l2 = ''.join(str(_) for _ in l2)[::-1]
        # answer = list(str(int(l1)+int(l2)))[::-1]
        # cursor = 0
        _len = max(len(l1), len(l2))
        upper = 0
        for i in range(_len):
            x = 0
            y = 0
            if i < len(l1):
                x = l1[i]
            if i < len(l2):
                y = l2[i]

            answer.append((x+y+upper)%10)
            upper = (x+y+upper) // 10    
        
        if upper >0:
            answer.append(1)
        return answer



solution = Solution()
# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [0]
# l2 = [0]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(solution.addTwoNumbers(l1=l1, l2=l2))

        