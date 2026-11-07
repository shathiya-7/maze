from collections import deque
import time

def dfs(grid, start, goal, terrain_costs):
    start_time = time.perf_counter()
    rows, cols = len(grid), len(grid[0])
    stack = [start]
    visited = {start}
    parent = {start: None}
    nodes_explored = 0
    events = []

    events.append({"type": "start", "cell": start})

    while stack:
        current = stack.pop()
        nodes_explored += 1
        events.append({"type": "explore", "cell": current})

        if current == goal:
            events.append({"type": "goal_found", "cell": goal})
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] != "WALL":
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append(neighbor)
                    events.append({"type": "discover", "cell": neighbor})

    end_time = time.perf_counter()
    
    if goal not in parent:
        return {"path": [], "cost": float("inf"), "nodes_explored": nodes_explored, "execution_time": end_time - start_time, "events": events}

    path = []
    curr = goal
    total_cost = 0
    while curr:
        path.append(curr)
        p = parent[curr]
        if p:
            total_cost += terrain_costs.get(grid[curr[0]][curr[1]], 1)
        curr = p
    
    final_path = path[::-1]
    for cell in final_path:
        events.append({"type": "path", "cell": cell})
    
    return {"path": final_path, "cost": total_cost, "nodes_explored": nodes_explored, "execution_time": end_time - start_time, "events": events}
