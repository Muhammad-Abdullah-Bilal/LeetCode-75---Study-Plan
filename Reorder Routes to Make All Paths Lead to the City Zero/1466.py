class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))   
            graph[b].append((a, 0))  

        visited = set()
        changes = 0

        def dfs(city):
            nonlocal changes
            visited.add(city)

            for nei, cost in graph[city]:
                if nei not in visited:
                    changes += cost 
                    dfs(nei)

        dfs(0)
        return changes
