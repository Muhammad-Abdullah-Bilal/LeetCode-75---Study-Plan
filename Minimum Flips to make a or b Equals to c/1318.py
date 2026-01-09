class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        while a > 0 or b > 0 or c > 0:
            ai = a & 1
            bi = b & 1
            ci = c & 1
            
            if ci == 1:
                if ai == 0 and bi == 0:
                    flips += 1
            else:
                flips += ai + bi
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips