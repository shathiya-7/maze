import heapq
import time

def ucs(grid, start, goal, terrain_costs):
    start_time = time.perf_counter()
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start)]
    visited = {} 
    parent = {start: None}
    nodes_explored = 0
    events = []

    events.append({"type": "start", "cell": start})

    while pq:
        cost, current = heapq.heappop(pq)
        if current in visited and visited[current] <= cost:
            continue
        visited[current] = cost
        nodes_explored += 1
        events.append({"type": "explore", "cell": current})
        if current == goal:
            events.append({"type": "goal_found", "cell": goal})
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                cell_type = grid[neighbor[0]][neighbor[1]]
                if cell_type != "WALL":
                    move_cost = terrain_costs.get(cell_type, 1)
                    new_cost = cost + move_cost
                    if neighbor not in visited or new_cost < visited[neighbor]:
                        parent[neighbor] = current
                        heapq.heappush(pq, (new_cost, neighbor))
                        events.append({"type": "discover", "cell": neighbor})

    end_time = time.perf_counter()
    if goal not in parent:
        return {"path": [], "cost": float("inf"), "nodes_explored": nodes_explored, "execution_time": end_time - start_time, "events": events}
    path = []
    curr = goal
    while curr:
        path.append(curr)
        curr = parent[curr]
    final_path = path[::-1]
    for cell in final_path:
        events.append({"type": "path", "cell": cell})
    return {"path": final_path, "cost": visited[goal] if goal in visited else float("inf"), "nodes_explored": nodes_explored, "execution_time": end_time - start_time, "events": events}
