class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # n=len(s)
        # if len(set(s))==1 or n==k:
        #     return s
        
        # newStr=s*(k+1)
        # return newStr[k:k+n]


        newStr=""
        for i in range(len(s)):
            newStr+=s[(i+k)%len(s)]

        return newStr