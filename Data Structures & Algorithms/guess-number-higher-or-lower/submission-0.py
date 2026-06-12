class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        while l<=r:
            mid=(l+r)//2
            result = guess(mid)
            if result==0:
                return mid
            elif result==1:
                l= mid+1
            elif result==-1:
                r= mid-1
        