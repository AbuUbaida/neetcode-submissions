class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for n in nums:
            if n!=val:
                count+=1
        if count>0:
            nums.remove(val)
            nums+=[val]*2
        return count