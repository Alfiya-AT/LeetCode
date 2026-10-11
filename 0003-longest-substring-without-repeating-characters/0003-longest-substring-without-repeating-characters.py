class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left=0
        right=0

        seen=[]

        maxLen=0
        while right<len(s):
            if s[right] in seen:
                while s[left]!=s[right]:
                    seen.remove(s[left])
                    left+=1
                seen.remove(s[left])
                left+=1
            seen.append(s[right])
            maxLen=max(maxLen,right-left+1)
            right+=1

        return maxLen
























        # d={}
        # start=0
        # maxLen=0
        # for end,val in enumerate(s):
        #     if val in d and d[val]>=start:
        #         start=d[val]+1
        #     d[val]=end
            
        #     maxLen=max(maxLen,end-start+1)


        # return maxLen


        # if len(s)<=0:
        #     return 0
        # elif len(s)==1:
        #     return 1
        # elif len(s)==len(set(s)):
        #     return len(s)
        # seen=set()
        # right=0
        # left=0
        # maxLen=0
        # while right<len(s):
        #     if s[right] in seen:
        #         while left<right and s[left]!=s[right]:
        #             seen.remove(s[left])
        #             left+=1
        #         left+=1
        #     maxLen=max(maxLen,right-left+1)
               
        #     seen.add(s[right])
        #     right+=1
            
        # return maxLen




