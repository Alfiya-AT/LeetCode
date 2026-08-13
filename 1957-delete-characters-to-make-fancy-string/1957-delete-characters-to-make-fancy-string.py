class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=2:
            return s
        
        left=0
        right=2
        res=''
        while right<len(s):
            if s[left]!=s[left+1] or s[left]!=s[right]:
                res+=s[left]
            left+=1
            right+=1
        return res+s[-2:]