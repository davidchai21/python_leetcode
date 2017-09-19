class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=1
        while a<=num:
            a<<=1
        return (a-1)^num