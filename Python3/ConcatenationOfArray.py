class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0] * 2 * nums_len
        for i in range(nums_len):
            ans[i] = nums[i]
            ans[i + nums_len] = nums[i]

        return ans