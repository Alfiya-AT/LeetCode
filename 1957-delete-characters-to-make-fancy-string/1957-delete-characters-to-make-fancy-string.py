class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """

        l=[]
        for ch in s:
            if len(l)<2 or ch!=l[-1] or ch!=l[-2]:
                l.append(ch)

        return "".join(l)

        # if len(s)<=2:
        #     return s
        
        # left=0
        # right=2
        # res=''
        # while right<len(s):
        #     if s[left]!=s[left+1] or s[left]!=s[right]:
        #         res+=s[left]
        #     left+=1
        #     right+=1
        # return res+s[-2:]