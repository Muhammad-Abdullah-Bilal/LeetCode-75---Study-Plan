from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        for i, ch in enumerate(senate):
            if ch == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)        
        n = len(senate)
        while r_queue and d_queue:
            r_index = r_queue.popleft()
            d_index = d_queue.popleft()
            if r_index < d_index:
                r_queue.append(r_index + n)
            else:
                d_queue.append(d_index + n)
        
        return "Radiant" if r_queue else "Dire"
 