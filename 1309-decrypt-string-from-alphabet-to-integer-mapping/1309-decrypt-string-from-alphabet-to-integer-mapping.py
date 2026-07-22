class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        # res=chr(96+1)
        i=len(s)-1
        while i>=0:
            if s[i]=='#':
                val=int(s[i-2:i])
                ans+=chr(96+val)
                i-=3
            else:
                val=int(s[i])
                ans+=chr(96+val)
                i-=1
        return ans[::-1]