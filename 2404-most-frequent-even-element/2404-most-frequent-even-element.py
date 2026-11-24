class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        d={}
        for key in nums:
            d[key]=d.get(key,0)+1
        
        sortedD=sorted(d.items(),key=lambda item:(-item[1],item[0]))

        res=[key for key,count in sortedD if key%2 == 0]
        return res[0] if res else -1