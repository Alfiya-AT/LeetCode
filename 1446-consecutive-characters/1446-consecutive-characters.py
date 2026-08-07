class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=1
        curr=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curr+=1
                freq=max(freq,curr)
            else:
                curr=1 
        return freq