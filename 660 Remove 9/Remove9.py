class Solution:
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=""
        while n>0:
            s=str(n%9)+s
            n=n//9
        return int(s)