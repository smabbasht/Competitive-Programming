class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        offset = 0
        while(len(nums)>1):
            print(nums)
            index = len(nums)//2
            if (nums[index]>target):
                nums = nums[:index]
            elif (nums[index]<target):
                offset += index
                nums = nums[index:]
            elif (nums[index]==target):
                return index+offset
        return -1 + (offset+1)*(nums[0]==target)
                