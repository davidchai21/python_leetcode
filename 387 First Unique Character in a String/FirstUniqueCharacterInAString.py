class Solution(object):
    def firstUniqChar(self, s):
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
        flag=False
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
                flag=True
        if flag==False:
            return -1