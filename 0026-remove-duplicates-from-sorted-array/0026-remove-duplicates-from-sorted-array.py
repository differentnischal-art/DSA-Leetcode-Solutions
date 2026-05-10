# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     nums.remove(nums[j])
#                 else:
#                     nums.sort()
#         k=len(nums)
#         return k
        #this is how I tried but I was showing index out of range so 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):        # while loop instead of for
            j = i + 1
            while j < len(nums):    # while loop instead of for
                if nums[i] == nums[j]:
                    nums.remove(nums[j])  # safe now, j rechecks length
                else:
                    j += 1          # only move j if no removal
            i += 1
        
        k = len(nums)
        return k
##the reason why previous code  didnt work because it didnt update the values of len(nums) 
#        Original: [0, 0, 1, 1, 2]  len=5
# range(0,5) is locked → j will try to reach index 4

# i=0, j=1 → nums[0]==nums[1] → remove → [0, 1, 1, 2]  len=4
                                                  
# now array has 4 elements (indices 0-3)
# but range still thinks len=5

# i=0, j=2 → fine
# i=0, j=3 → fine
# i=1, j=4 → CRASH ❌ index 4 doesn't exist anymore
        