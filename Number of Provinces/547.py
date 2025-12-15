class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        provinces = 0
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1

        return provinces
