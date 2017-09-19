class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res=0
        t=x^y
        # t&=t-1
        while t:
            res+=1
            t&=t-1
        return res