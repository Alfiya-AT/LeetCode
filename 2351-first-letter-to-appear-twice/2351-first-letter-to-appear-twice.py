class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in s:
            if i in d:
                return i
            d[i]=d.get(i,0)+1
        
