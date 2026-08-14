class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        freq={}
        left=0
        maxLength=0

        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1

            while freq[s[right]]>2:
                freq[s[left]]-=1
                left+=1

            maxLength=max(maxLength,right-left+1)
        
        return maxLength






        # mx=1
        # left=0
        # right=0
        # n=len(s)
        # i=0
        # while right-left!=n-1:
        #     while right<n:
        #         if len(s[left:right+1])==len(set(s[left:right+1])):
        #             mx=max(mx,len(s[left:right+1]))
        #         left+=1
        #         right+=1
        #     i+=1
        #     left=0
        #     right=i
        # return mx+1