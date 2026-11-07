import random

class MazeGenerator:
    def __init__(self, rows=20, cols=20):
        self.rows = rows
        self.cols = cols

    def generate_recursive_backtracking(self, wall_density=0.2):
        # Grid must be odd for recursive backtracking to work perfectly with walls
        rows = self.rows if self.rows % 2 != 0 else self.rows + 1
        cols = self.cols if self.cols % 2 != 0 else self.cols + 1
        
        grid = [["WALL" for _ in range(cols)] for _ in range(rows)]
        
        def get_neighbors(r, c):
            neighbors = []
            for dr, dc in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbors.append((nr, nc))
            return neighbors

        start_r, start_c = 0, 0
        grid[start_r][start_c] = "EMPTY"
        stack = [(start_r, start_c)]
        visited = {(start_r, start_c)}

        while stack:
            curr_r, curr_c = stack[-1]
            neighbors = [n for n in get_neighbors(curr_r, curr_c) if n not in visited]
            
            if neighbors:
                next_r, next_c = random.choice(neighbors)
                grid[(curr_r + next_r) // 2][(curr_c + next_c) // 2] = "EMPTY"
                grid[next_r][next_c] = "EMPTY"
                visited.add((next_r, next_c))
                stack.append((next_r, next_c))
            else:
                stack.pop()

        grid[0][0] = "START"
        grid[rows-1][cols-1] = "GOAL"
        
        # Connect goal to the maze
        if grid[rows-2][cols-1] == "WALL" and grid[rows-1][cols-2] == "WALL":
            if rows > cols: grid[rows-2][cols-1] = "EMPTY"
            else: grid[rows-1][cols-2] = "EMPTY"

        # Add weighted terrain
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "EMPTY" and random.random() < wall_density:
                    grid[r][c] = random.choice(["MUD", "WATER"])

        return grid
