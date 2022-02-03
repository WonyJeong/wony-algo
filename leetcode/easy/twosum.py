def twoSum(self, nums : List[int], target : int) -> List[int]:
    for i in range(nums.length):
        for j in range(1, nums.length):
            if nums[i] + nums[j] == target:
                return [i,j]
