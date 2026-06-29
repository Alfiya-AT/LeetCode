class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for ch in words:
            if ch == ch[::-1]:
                return ch

        return ""