class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        upper=set('qwertyuiop')
        middle=set('asdfghjkl')
        lower=set('zxcvbnm')
        ans=[]
        for word in words:
            t=set(word.lower())
            if t&upper==t:
                ans.append(word)
            elif t&middle==t:
                ans.append(word)
            elif t&lower==t:
                ans.append(word)
        return ans
                