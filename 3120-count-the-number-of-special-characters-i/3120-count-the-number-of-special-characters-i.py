class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        charSet=set(word)
        count=0

        alpha="abcdefghijklmnopqrstuvwxyz"

        for char in alpha:
            if char in charSet and char.upper() in charSet:
                count+=1

        return count