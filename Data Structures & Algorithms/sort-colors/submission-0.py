class Solution:
    def sortColors(self, nums: List[int]) -> None:

        if len(nums)==1:
            return nums

        left = 0

        for i in range(3):
            for right in range(len(nums)):
                if nums[right]==i:
                    nums[left], nums[right]= nums[right],nums[left]
                    left = left+1
        return nums