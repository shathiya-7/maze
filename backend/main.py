from typing import List, Tuple

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

if __package__:
    from .game.engine import GameEngine
    from .maze.generator import MazeGenerator
    from .maze.terrain import get_terrain_costs
else:
    from game.engine import GameEngine
    from maze.generator import MazeGenerator
    from maze.terrain import get_terrain_costs

app = FastAPI(title="AI Maze Solver API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = GameEngine()

class SolveRequest(BaseModel):
    algorithm: str
    grid: List[List[str]]
    start: Tuple[int, int]
    goal: Tuple[int, int]

class CompareRequest(BaseModel):
    grid: List[List[str]]
    start: Tuple[int, int]
    goal: Tuple[int, int]

@app.post("/api/maze/generate")
def generate_maze(rows: int = 21, cols: int = 21, density: float = 0.2):
    gen = MazeGenerator(rows, cols)
    grid = gen.generate_recursive_backtracking(wall_density=density)
    return {"grid": grid, "rows": len(grid), "cols": len(grid[0])}

@app.post("/api/solve")
def solve_maze(req: SolveRequest):
    try:
        return engine.solve(req.algorithm, req.grid, req.start, req.goal, get_terrain_costs())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/compare")
def compare_algos(req: CompareRequest):
    algorithms = ["BFS", "DFS", "UCS", "A*"]
    results = {}
    costs = get_terrain_costs()
    for algo in algorithms:
        results[algo] = engine.solve(algo, req.grid, req.start, req.goal, costs)
    return results
