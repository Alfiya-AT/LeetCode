class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        
        if len(s)!=len(words):
            return False

        for i,c in enumerate(s):
            if words[i][0]!=c:
                return False
        return True