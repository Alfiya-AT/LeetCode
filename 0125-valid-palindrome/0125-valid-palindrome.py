class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1

        while i<j:
            left=s[i]
            right=s[j]

            while left.isalnum()==False and i<j:
                i+=1
                left=s[i]

            while right.isalnum()==False and i<j:
                j-=1
                right=s[j]  

            if left.isalnum() and right.isalnum():
                if left.lower()!=right.lower():
                    return False

            i+=1
            j-=1
        return True