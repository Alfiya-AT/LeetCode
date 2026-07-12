class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        
        n=len(words)
        j=0
        if n>len(s) or len(s)>n:
            return False
        for i in s:
            if j<n and i == words[j][0]:
                j+=1
            else:
                return False
        return True