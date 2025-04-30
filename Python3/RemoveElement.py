# First Attempt
# Reason for failure: Does not consider arrays of size 1 or less
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        # While our two pointers haven't met
        while (l < r):
            # if our left pointer is on a value that needs to be replaced
            if nums[l] == val:
                # if our right pointer is a value we also need to replace
                if nums[r] == val:
                    # get rid of it and decrement
                    nums.pop(r)
                    r -= 1
                else:
                    # but if our right pointer is a value we want to keep, move it over
                    nums[l] = nums[r]
                    r -= 1
            else:
                # if our left pointer shouldnt be replaced, then move until we find one that does need replaced
                l += 1
        
        return l+1
    
# Second Attempt
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            # if our i pointer is a value we want to keep
            if nums[i] != val:
                # then replace our k pointer with that value
                # this works because they move together
                # so if it doesn't need replaced, it will get replaced with itself
                nums[k] = nums[i]
                k += 1

        return k