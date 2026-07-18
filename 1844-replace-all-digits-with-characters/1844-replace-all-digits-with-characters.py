class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        
        for ch in s:
            if ch.isdigit():
                res+=chr(ord(prev)+int(ch))
            else:
                res+=ch
                prev=ch

        return res