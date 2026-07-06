class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        res=[]
        for key,val in d.items():
            res.append(val)

        return len(set(res))==len(res)