class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr1=[i for i in arr]
        arr1.sort()
        d={}
        count=1
        for i in arr1:
            if i not in d:
                d[i]=count
                count+=1
        res=[]
        for i in arr:
            res.append(d[i])
        return res