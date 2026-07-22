class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=[int(x) for x in s]
        return self.same(s)
        
    def same(self,s):
        if len(s)==2 and s[0]==s[1]:
            return True
        elif len(s)==2 and s[0]!=s[1]:
            return False
        else:
            res=[]
            sum=s[0]
            for i in range(1,len(s)):
                sum+=s[i]
                res.append(sum%10)
                sum-=s[i-1]
            return self.same(res)
        
            


