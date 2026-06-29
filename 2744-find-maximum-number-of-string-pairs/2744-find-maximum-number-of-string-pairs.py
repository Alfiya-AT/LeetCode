class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        rev=[x[::-1] for x in words]
        count=0
        for ch in range(len(words)):
            if words[ch] in rev[ch+1:]:
                count+=1
        return count
        