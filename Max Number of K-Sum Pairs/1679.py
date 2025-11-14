class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        oper = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                oper += 1
                l += 1
                r -= 1
            elif s < k:
               l += 1
            else:
                r -= 1

        return(oper)
