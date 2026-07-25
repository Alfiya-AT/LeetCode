class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        dt={}
        ds={}
        for ch in s:
            ds[ch]=ds.get(ch,0)+1
        for t in target:
            dt[t]=dt.get(t,0)+1
        minVal=float('Inf')
        for key,value in dt.items():
            if key not in ds:
                return 0
            else:
                val=ds[key]//dt[key]
                minVal=min(minVal,val)
        return minVal