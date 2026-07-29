class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        half=len(s)//2
        start="".join(sorted(s[:half]))

        if len(s)%2!=0:
            mid=s[half]
        else:
            mid=""

        return start+mid+start[::-1]