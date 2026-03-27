class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0,len(nums)-1):
            for j in range(i+1,len(nums)):
                current_sum=nums[i]+nums[j]
                if current_sum==target:
                    return [i,j]
        