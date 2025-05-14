# BucketSort solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First, make our buckets
        buckets = [0, 0, 0]

        # We are kind of cheating here since the numerical representations
        # Can easily line up with our indices, but this isn't always the case
        for color in nums:
            buckets[color] += 1
        
        # Cur will track where we are in the original array
        cur = 0
        # For every bucket
        for b in range(0, len(buckets)):
            # We want to make the specified amount of indices in the nums array
            # the corresponding color number
            for c in range(0, buckets[b]):
                nums[cur] = b
                cur += 1
            
# One pass solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We need a pointer at the left and right of our array
        left, right = 0, len(nums) - 1
        # And then one to keep track of our current index
        i = 0
        
        # While we haven't crossed the right pointer
        while i <= right:
            # Two cases we care about, [i] == 0, or [i] == 2, because then we swap
            if nums[i] == 0:
                # Store whats in our left pointer
                tmp = nums[left]
                # Change our left pointer value to the value we're swapping
                nums[left] = nums[i]
                # Put the value that was in our left pointer at our index
                nums[i] = tmp
                # Then increment
                left += 1

            elif nums[i] == 2:
                # Store what's in our right pointer
                tmp = nums[right]
                # Change our right pointer to the value we're swapping
                nums[right] = nums[i]
                # Put the value tha twas in our right pointer at our index
                nums[i] = tmp
                # Then decrement
                right -= 1
                # This is a special case, if we swapped a value from the right we DON'T wanna increment i
                # Because we might have just put a 0 into the middle of our array, if we did then we need
                # to look at it again
                i -= 1
            i += 1