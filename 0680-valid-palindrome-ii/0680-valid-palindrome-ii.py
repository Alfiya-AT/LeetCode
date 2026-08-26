class Solution(object):
    def PalindromeHelper(self,i,j,s):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1

        while i<=j:
            left=s[i]
            right=s[j]
            if left!=right:
                return self.PalindromeHelper(i+1,j,s) or self.PalindromeHelper(i,j-1,s)
            else:
                i+=1
                j-=1
                
        return True