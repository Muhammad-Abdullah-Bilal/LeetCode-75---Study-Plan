# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         dic = {}
#         for num in arr:
#             if num in dic:
#                 dic[num] += 1
#             else:
#                 dic[num] = 1

#         seen = set()
#         for value in dic.values():
#             if value in seen:
#                 return False
#             else:
#                 seen.add(value)

#         return True 


# Other Method
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {} 
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1 
        
        values = list(freq.values())
        if len(values) == len(set(values)):
            return True
        else:
            return False
