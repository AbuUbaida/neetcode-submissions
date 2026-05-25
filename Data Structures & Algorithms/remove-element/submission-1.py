class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i]==val:
                popped = nums.pop(i)
                nums.append(popped)
                count+=1
                i+=1
        return len(nums)-count