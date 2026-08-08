class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        mx=0
        for i in strs:
            if i.isdigit():
                mx=max(mx,int(i))
            else:
                mx=max(mx,len(i))
            
        return mx