class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceLength= defaultdict(int)
        longest =0

        for num in nums:
            if not sequenceLength[num]:
                leftLength=sequenceLength[num-1]
                rightLength=sequenceLength[num+1]

                currentLength=leftLength+rightLength+1
                sequenceLength[num]=currentLength

                sequenceLength[num-leftLength]=currentLength
                sequenceLength[num+rightLength]=currentLength

                longest = max(longest,currentLength)

        return longest