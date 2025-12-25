class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            target = (success + spell - 1) // spell

            left, right = 0, m - 1
            ans = m  

            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            result.append(m - ans)

        return result
