from collections import Counter
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        if letter not in s:
            return 0

        n=len(s)
        d=Counter(s)
        m=d[letter]
        res=(m*100)//n
        return res
        
