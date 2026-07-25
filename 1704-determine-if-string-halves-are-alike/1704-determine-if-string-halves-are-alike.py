class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels="aeiou"
        ans=[0]*len(s)
        for i in range(len(s)):
            ch=s[i]
            if ch.lower() in vowels:
                ans[i]=1
        mid=len(s)//2
        return sum(ans[:mid])==sum(ans[mid:])