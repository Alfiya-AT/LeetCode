class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={}
        for ch in s:
            d[ch]=d.get(ch,1)+1
        
        res=[]
        for val in d.values():
            res.append(val)
        return len(set(res))==1