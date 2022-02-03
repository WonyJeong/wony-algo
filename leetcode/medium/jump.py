def canJump(nums):
    end = len(nums) - 1
    dp = [0] * len(nums)
    dp[0] = nums[0]
    i = 0
    _max = -1

    if(end == 0):
        return True
    
    if(end == 1):
        if nums[0] > 0:
            return True
        else:
            return False

    for i in range(0, len(nums) - 2):
        for j in range(i, i + nums[i] + 1):
            dp[j] = j + nums[j]
            _max = max(_max, dp[j])
            if _max >= end:
                return True
        if _max > j:
            i = j
        else:
            break
    return False
    
if __name__ == "__main__":
    print(canJump([3,2,1,0,4]), False) 
