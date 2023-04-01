class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for ind, num in enumerate(nums[:-1]):
            for indx, numx in enumerate(nums[ind+1:]):
                if num+numx == target:
                    return [ind, indx+1+ind]
                