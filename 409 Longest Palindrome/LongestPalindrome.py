class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        even=0
        odd=0
        for k in d:
            if d[k]%2:
                odd=1
                even+=d[k]-1
            else:
                even+=d[k]
        return odd+even