class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # While our left has not surpassed our right
        while left <= right:
            # Find the midpoint
            mid = int((left + right) / 2)

            # If we're in the right half, reduce our search range to that half
            if nums[mid] < target:
                left = mid + 1

            # IF we're in the left half, reduce our search range to that half
            elif nums[mid] > target:
                right = mid - 1

            # If we are the target, then we're done!
            else:
                return mid
        return -1