import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left = 0
        right = n - 1

        left_heap = []
        right_heap = []

        for _ in range(candidates):
            if left > right:
                break
            heapq.heappush(left_heap, costs[left])
            left += 1

        for _ in range(candidates):
            if left > right:
                break
            heapq.heappush(right_heap, costs[right])
            right -= 1

        total = 0

        for _ in range(k):
            if right_heap and left_heap:
                if left_heap[0] <= right_heap[0]:
                    total += heapq.heappop(left_heap)
                    if left <= right:
                        heapq.heappush(left_heap, costs[left])
                        left += 1
                else:
                    total += heapq.heappop(right_heap)
                    if left <= right:
                        heapq.heappush(right_heap, costs[right])
                        right -= 1

            elif left_heap:
                total += heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1

            else:
                total += heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return total
