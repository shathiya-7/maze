# AI Maze Solving Robot

An academic demonstration of AI search algorithms.

## Setup
### Backend
1. `cd maze`
2. `pip install -r backend/requirements.txt`
3. `uvicorn backend.main:app --reload`

### Frontend
1. `cd maze/frontend`
2. `npm install`
3. `npm run dev`

## AI Theory
- **BFS**: Guarantees shortest path in unweighted grids.
- **DFS**: Deep exploration, non-optimal path.
- **UCS**: Lowest total cost path (handles mud/water).
- **A***: Heuristic-driven (Manhattan distance) for efficiency.

