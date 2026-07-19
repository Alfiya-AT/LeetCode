class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        res=[]
        for word in words:
            parts=word.split(separator)
            for part in parts:
                if part:
                    res.append(part)


        return res