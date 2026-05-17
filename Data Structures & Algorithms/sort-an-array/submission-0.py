class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                else:
                    j = j+1
        return nums
        