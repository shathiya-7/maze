from ..ai.astar import astar
from ..ai.bfs import bfs
from ..ai.dfs import dfs
from ..ai.ucs import ucs
from .scoring import ScoringSystem


class GameEngine:
    def __init__(self):
        self.scoring = ScoringSystem()

    @staticmethod
    def _normalize_algorithm(algorithm):
        if algorithm is None:
            raise ValueError("Algorithm is required")

        normalized = str(algorithm).strip()
        if not normalized:
            raise ValueError("Algorithm is required")

        alias_map = {
            "BFS": "BFS",
            "DFS": "DFS",
            "UCS": "UCS",
            "A*": "A*",
            "ASTAR": "A*",
            "A_STAR": "A*",
        }

        candidate = normalized.upper().replace("_", "")
        if candidate in {"ASTAR", "A"}:
            return "A*"
        return alias_map.get(normalized.upper(), alias_map.get(candidate, normalized.upper()))

    def solve(self, algorithm, grid, start, goal, terrain_costs):
        normalized = self._normalize_algorithm(algorithm)

        if normalized == "BFS":
            return bfs(grid, start, goal, terrain_costs)
        if normalized == "DFS":
            return dfs(grid, start, goal, terrain_costs)
        if normalized == "UCS":
            return ucs(grid, start, goal, terrain_costs)
        if normalized == "A*":
            return astar(grid, start, goal, terrain_costs)

        raise ValueError(f"Unsupported algorithm: {algorithm}")
