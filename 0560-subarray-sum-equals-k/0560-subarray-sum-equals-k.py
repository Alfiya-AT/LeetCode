class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        prefixSum=0
        count=0
        
        for i in range(len(nums)):
            prefixSum+=nums[i]

            if prefixSum-k in seen:
                 count+=seen[prefixSum-k]
            
            seen[prefixSum]=seen.get(prefixSum,0)+1
    
        return count