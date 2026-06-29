class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count=0
        for c in words:
            if c>=len(pref) and c[:len(pref)]==pref:
                count+=1
        return count
        