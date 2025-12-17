class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(start, end, visited, value):
            if start == end:
                return value
            visited.add(start)

            for nei, weight in graph[start]:
                if nei not in visited:
                    result = dfs(nei, end, visited, value * weight)
                    if result != -1:
                        return result
            return -1

        results = []
        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(a, b, set(), 1.0))

        return results

        