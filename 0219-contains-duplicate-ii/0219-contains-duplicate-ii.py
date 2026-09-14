class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen=set()
        right=0
        left=0
        # while right<k:
        #     if nums[right] in seen:
        #         return True
        #     seen.add(nums[right])
        #     right+=1
        
        while right<len(nums):
            if nums[right] in seen:
                
                while left<right and nums[left]!=nums[right]:
                    seen.remove(nums[left])
                    left+=1
                
                if right-left<=k:
                    return True
                left+=1
            seen.add(nums[right])
                
            
            right+=1
        return False