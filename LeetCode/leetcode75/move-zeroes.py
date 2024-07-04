class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        n = 0
        while ind<len(nums):
            if nums[ind]==0:
                nums.pop(ind)
                n+=1
            else:
                ind+=1
        nums += [0]*n
        
        
