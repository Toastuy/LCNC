class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Left will be tracking our unique numbers and the index of where the next unique number needs to go
        # As we go through the array with right, we will know if we are a duplicate and can be skipped,
        # Or if we are a unique value and need to increment and move said unique value to our left index
        left = right = 0

        # While our right pointer scans
        while right < len(nums):
            # If it's a duplicate to our current unique value, we just move along
            if nums[right] == nums[left]:
                right += 1
            # Otherwise, we have a new unique value and need to move it
            elif nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        # Since left is an index, we need to add 1 before returning to get the actual number of uniques
        left += 1
        return left