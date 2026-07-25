class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        if len(s)%k!=0:
            val=k-(len(s)%k)
            s=s+(val*fill)
        ans=[]
        left=0
        right=k-1
        while right<len(s):
            ans.append(s[left:right+1])
            left=right+1
            right+=k
        return ans