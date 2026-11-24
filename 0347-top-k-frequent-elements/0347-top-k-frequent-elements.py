class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        for key in nums:
            d[key]=d.get(key,0)+1

        sortedD=sorted(d.items(),key=lambda item: (-item[1],item[0]))
        res=[]
        for key,val in sortedD[:k]:
            res.append(key)
        return res