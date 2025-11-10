class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0  
        i = 0  
        while i < len(chars):
           char = chars[i]
           count = 0
           while i < len(chars) and chars[i] == char:
              i += 1
              count += 1
           chars[w] = char
           w += 1
        
           if count > 1:
            for c in str(count):
                chars[w] = c
                w += 1
    
        return w