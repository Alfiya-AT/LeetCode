class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel="aeiou"
        i=len(s)-1
        while s[i] in vowel and i>=0:
            i-=1
        return s[:i+1]