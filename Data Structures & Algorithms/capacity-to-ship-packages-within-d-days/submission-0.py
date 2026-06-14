class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right=max(weights),sum(weights)
        while left<right:
            capacity=(left+right)//2
            days_needed=1
            current_weight=0
            for weight in weights:
                if current_weight+weight>capacity:
                    days_needed+=1
                    current_weight=0
                current_weight+=weight
            if days_needed<=days:
                right=capacity
            else:
                left=capacity+1
        return left
                
        