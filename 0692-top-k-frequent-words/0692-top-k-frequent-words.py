class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d={}

        for key in words:
            d[key]=d.get(key,0)+1


        s=sorted(d.items(),key = lambda item : ((-item[1],item[0])))


        res=[]
        for key,val in s[:k]:
            res.append(key)
        return res