class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1=1000
        l2=1000
        r1=-1000
        r2=-1000
        r3=-1000
        for i in nums:
            if i<l1:
                l2=l1
                l1=i
            elif i<l2 and i>=l1:
                l2=i
            if i>r1:
                r3=r2
                r2=r1
                r1=i
            elif i<=r1 and i>r2:
                r3=r2
                r2=i
            elif i>r3 and i<=r2:
                r3=i
        return max(l1*l2*r1,r1*r2*r3)