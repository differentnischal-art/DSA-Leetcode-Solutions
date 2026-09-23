class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0

        # 1. Create first window
        for i in range(k):
            sum = sum + nums[i]

        max_sum = sum

        # 2. Slide window
        for i in range(k, len(nums)):
            sum = sum + nums[i] - nums[i-k]

            if sum > max_sum:
                max_sum = sum
        return max_sum / k

                


    
        