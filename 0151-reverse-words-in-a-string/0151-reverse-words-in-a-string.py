class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        trim=s.strip()
        arr=trim.split()

        return " ".join(arr[::-1])