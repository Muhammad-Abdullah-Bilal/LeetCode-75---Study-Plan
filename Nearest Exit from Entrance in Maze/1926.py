class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque

        m, n = len(maze), len(maze[0])
        start_r, start_c = entrance

        queue = deque()
        queue.append((start_r, start_c, 0))  
        visited = set()
        visited.add((start_r, start_c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c, steps = queue.popleft()

            if (r == 0 or r == m-1 or c == 0 or c == n-1) and [r, c] != entrance:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if maze[nr][nc] == '.' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

        return -1
