class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        
        def getallsubset(nums, arr, i, seen):
            if i == len(nums):
                seen.append(arr.copy())
                return

            # Include the current element
            arr.append(nums[i])
            getallsubset(nums, arr, i + 1, seen)

            # Backtrack
            arr.pop()

            # Skip duplicate elements
            idx = i + 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1

            # Exclude the current element
            getallsubset(nums, arr, idx, seen)

        nums.sort()
        arr = []
        seen = []

        getallsubset(nums, arr, 0, seen)

        return seen