# 🤖 AI Maze Solving Robot

> An interactive web-based AI project that demonstrates and compares classical search algorithms by controlling a robot navigating through a dynamically generated maze.

The **AI Maze Solving Robot** models robot navigation as a **state-space search problem**. The robot starts from an initial position and must find a valid path to a goal while avoiding obstacles. The application visualizes the search process by displaying explored cells and the final path, allowing users to understand how different AI search strategies behave.

The project implements **BFS, DFS, Uniform Cost Search (UCS), and A\*** and compares them using metrics such as execution time, explored states, path length, and solution cost.

---

# 1. Problem Statement

Autonomous robots need to navigate through environments while finding suitable paths from their current position to a destination. Different search strategies can produce different results in terms of speed, number of states explored, path length, and movement cost.

This project simulates this problem using a grid-based maze.

The robot must:

- Start from a predefined starting cell.
- Navigate through the maze.
- Avoid blocked cells/walls.
- Reach the destination.
- Find a valid and efficient path.
- Visualize the search process.
- Allow different AI algorithms to solve the same maze.
- Compare the performance of the algorithms.

The project demonstrates how classical AI search techniques can be applied to an autonomous navigation problem.

---

# 2. Problem Formulation

The maze is represented as a **state-space search problem**.

## 2.1 Initial State

The initial state represents the robot's starting position.

For example, in a `20 × 20` maze:

```text
Start = (0, 0)
```

The robot begins at this cell with no previously explored states.

Formally:

```text
Initial State = Robot positioned at the Start cell
```

---

## 2.2 Goal State

The goal state is the destination cell that the robot must reach.

For example:

```text
Goal = (19, 19)
```

The search terminates successfully when:

```text
Current State == Goal State
```

Therefore:

```text
Goal State = Robot reaches the destination cell
```

---

## 2.3 State Space

Every traversable cell in the maze represents a possible state.

A state is represented using:

```text
(row, column)
```

For example:

```text
(0,0)
(0,1)
(1,0)
(1,1)
...
```

For a `20 × 20` maze, there can be up to:

```text
20 × 20 = 400
```

possible grid positions, although walls and unreachable cells reduce the effective state space.

---

## 2.4 Possible Actions

The robot can move in four directions:

```text
UP
DOWN
LEFT
RIGHT
```

For a state `(row, column)`, the possible neighboring states are:

```text
(row - 1, column)   → UP
(row + 1, column)   → DOWN
(row, column - 1)   → LEFT
(row, column + 1)   → RIGHT
```

Diagonal movement is not allowed.

---

## 2.5 Constraints

The robot must satisfy the following constraints:

### Maze Boundaries

The robot cannot move outside the grid.

```text
0 ≤ row < number_of_rows
0 ≤ column < number_of_columns
```

### Walls

The robot cannot move into blocked cells.

```text
Wall = non-traversable
```

### Valid Movement

Only four-directional movement is allowed.

### Goal Constraint

The robot must eventually reach the goal cell for a successful mission.

---

## 2.6 Movement Cost

To make the problem more realistic and demonstrate cost-based search, the maze can contain different terrain types.

| Terrain | Cost |
|---|---:|
| Normal | 1 |
| Mud | 3 |
| Water | 5 |
| Wall | Not traversable |

Therefore, two paths with the same number of steps may have different total costs.

The total solution cost is:

```text
Solution Cost = Sum of movement costs along the selected path
```

This is particularly useful for evaluating **Uniform Cost Search and A\***.

---

## 2.7 Heuristic Function

A heuristic is used by A* Search to estimate the remaining distance from the current state to the goal.

The project uses **Manhattan Distance**:

```text
h(n) = |row_current - row_goal|
     + |column_current - column_goal|
```

For example:

```text
Current = (3, 5)
Goal    = (8, 9)

h(n) = |3 - 8| + |5 - 9|
     = 5 + 4
     = 9
```

A* uses the evaluation function:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` = actual cost from the start to the current state
- `h(n)` = estimated cost from the current state to the goal
- `f(n)` = estimated total cost of the solution through that state

---

# 3. Algorithms Used

The project implements four classical AI search algorithms.

---

## 3.1 Breadth-First Search (BFS)

BFS explores states level by level.

It uses a **queue (FIFO)** data structure.

Conceptually:

```text
Start
 ↓
Explore all nearby cells
 ↓
Explore cells one level farther
 ↓
Continue until Goal
```

### Characteristics

- Uninformed search
- Does not use a heuristic
- Complete for finite state spaces
- Finds the shortest path in an unweighted maze
- Can explore many states

### Data Structure

```text
Queue
```

---

## 3.2 Depth-First Search (DFS)

DFS explores one path as deeply as possible before backtracking.

It uses a **stack (LIFO)**.

Conceptually:

```text
Start
 ↓
Go deeper
 ↓
Go deeper
 ↓
Dead end
 ↓
Backtrack
 ↓
Try another path
```

### Characteristics

- Uninformed search
- Does not use a heuristic
- Can find a solution without exploring the entire maze
- Does not guarantee the shortest path
- May produce a longer solution

### Data Structure

```text
Stack
```

---

## 3.3 Uniform Cost Search (UCS)

UCS always expands the state with the lowest accumulated path cost.

It uses a **priority queue**.

The priority is:

```text
g(n)
```

where `g(n)` represents the total cost from the starting state to the current state.

UCS is particularly useful when different terrain types have different movement costs.

For example:

```text
Path A:
10 normal cells
Cost = 10

Path B:
5 normal cells + 2 water cells
Cost = 5 + 10 = 15
```

Although Path B is shorter in terms of number of cells, UCS prefers Path A because its total movement cost is lower.

### Characteristics

- Cost-based search
- Does not use a heuristic
- Finds the minimum-cost solution when movement costs are non-negative
- Can explore more states than A*

### Data Structure

```text
Priority Queue
```

---

## 3.4 A* Search

A* combines the actual cost of reaching a state with an estimate of the remaining cost.

It uses:

```text
f(n) = g(n) + h(n)
```

where:

```text
g(n) = cost from Start → Current
h(n) = estimated cost Current → Goal
```

The project uses Manhattan Distance as the heuristic.

### Characteristics

- Informed search
- Uses a heuristic
- Prioritizes promising states
- Can significantly reduce unnecessary exploration
- Can find an optimal solution when the heuristic is admissible and consistent for the problem

### Data Structure

```text
Priority Queue
```

---

# 4. Algorithm Comparison

| Algorithm | Search Type | Data Structure | Heuristic | Optimal in Unweighted Maze | Cost-Aware |
|---|---|---|---|---|---|
| BFS | Uninformed | Queue | No | Yes | No |
| DFS | Uninformed | Stack | No | No | No |
| UCS | Uninformed | Priority Queue | No | Yes | Yes |
| A* | Informed | Priority Queue | Yes | Yes* | Yes |

`*` A* optimality depends on using an appropriate heuristic and cost model.

---

# 5. Implementation

## 5.1 Technology Stack

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

### Frontend

- React
- Vite
- Tailwind CSS
- JavaScript
- Framer Motion
- Lucide React

### Optional Database

- Supabase

### Testing

- Pytest

---

# 6. System Architecture

The project follows a frontend-backend architecture:

```text
                    USER
                     │
                     ▼
              React Frontend
                     │
                     │ HTTP / WebSocket
                     ▼
              Python Backend
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Maze Engine    AI Search     Game Engine
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
         BFS        UCS         A*
          │          │          │
          └──────────┼──────────┘
                     │
                     ▼
             Search Results
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Explored Cells   Path       Metrics
        │            │            │
        └────────────┼────────────┘
                     ▼
              React Visualization
```

The search algorithms are implemented in **Python**, while the frontend is responsible for displaying the search process and interacting with the user.

---

# 7. Search Visualization

One of the main features of the application is visualizing the states explored by the AI.

Instead of displaying only the final solution, each algorithm generates a sequence of search events.

For example:

```text
Start
 ↓
Explore (0,0)
 ↓
Explore (0,1)
 ↓
Explore (1,0)
 ↓
Explore (0,2)
 ↓
...
 ↓
Goal Found
 ↓
Path Reconstruction
 ↓
Robot follows final path
```

The frontend represents these states using different visual styles:

| State | Visualization |
|---|---|
| Unvisited | Empty cell |
| Wall | Blocked cell |
| Frontier | Highlighted cell |
| Explored | Highlighted/animated cell |
| Current | Active/pulsing cell |
| Path | Final highlighted route |
| Start | Robot starting position |
| Goal | Destination |

This allows users to visually understand how BFS, DFS, UCS, and A* explore the same problem differently.

---

# 8. Performance Evaluation

The project compares algorithms using several measurable parameters.

## 8.1 Execution Time

The execution time is measured using Python's high-resolution timer:

```python
time.perf_counter()
```

The time is recorded before and after the search algorithm executes.

```text
Execution Time =
End Time - Start Time
```

---

## 8.2 Number of Explored States

Every time an algorithm processes a new state, it is recorded.

For example:

```python
explored_order.append(current)
```

The total number of explored states is:

```python
len(explored_order)
```

This metric indicates how much of the state space the algorithm had to investigate before finding the solution.

---

## 8.3 Path Length

After reaching the goal, the algorithm reconstructs the final path.

The number of movements is:

```text
Path Length = Number of cells in path - 1
```

A smaller path length indicates fewer movements.

---

## 8.4 Solution Cost

For weighted terrain:

```text
Solution Cost =
Sum of movement costs for all cells in the final path
```

This metric is particularly important for comparing BFS with UCS and A*.

BFS may find a path with fewer steps, while UCS or A* may find a path with lower total cost.

---

## 8.5 Maximum Frontier Size

The project can also record the maximum number of states stored in the frontier during the search.

This provides an indication of the algorithm's memory requirements.

---

# 9. Algorithm Comparison

The application includes an **Algorithm Lab** where all algorithms are run on the **same maze**.

The comparison process is:

```text
Generate Maze
      │
      ▼
Keep maze fixed
      │
 ┌────┼────┬────┐
 ▼    ▼    ▼    ▼
BFS  DFS  UCS  A*
 │    │    │    │
 ▼    ▼    ▼    ▼
Metrics collected
      │
      ▼
Comparison Dashboard
```

The same:

- maze
- start state
- goal state
- movement rules
- terrain costs

are used for every algorithm.

This ensures a fair comparison.

---

# 10. Performance Metrics

The comparison dashboard displays:

| Metric | Description |
|---|---|
| Execution Time | Time required to complete the search |
| Explored States | Number of states expanded |
| Path Length | Number of movements in the solution |
| Solution Cost | Total cost of the selected path |
| Frontier Size | Maximum states stored for exploration |

Example output:

| Algorithm | Time | Explored | Path Length | Cost |
|---|---:|---:|---:|---:|
| BFS | 2.1 ms | 143 | 32 | 58 |
| DFS | 1.7 ms | 91 | 57 | 72 |
| UCS | 3.4 ms | 168 | 36 | 41 |
| A* | 1.9 ms | 87 | 36 | 41 |

> The values above are illustrative. The application calculates the actual values dynamically for each generated maze.

---

# 11. Results

The results depend on the structure of the generated maze and the distribution of terrain costs.

Generally, the following behavior is expected:

### BFS

BFS is effective in an unweighted maze because it explores states level-by-level and finds the shortest path in terms of number of moves.

However, it may explore many unnecessary states.

### DFS

DFS can reach the goal quickly if it chooses a favorable path.

However, it may follow an inefficient route and does not guarantee the shortest or lowest-cost solution.

### UCS

UCS considers the accumulated movement cost.

It is therefore more suitable when the maze contains different terrain costs.

It may explore more states because it does not have a heuristic to guide it toward the goal.

### A*

A* uses both the actual path cost and the heuristic estimate.

```text
f(n) = g(n) + h(n)
```

Therefore, it can focus its search toward promising regions of the maze while still considering path cost.

For suitable heuristics, A* can produce an optimal solution while exploring fewer states than uninformed approaches.

---

# 12. Expected Observations

The project can demonstrate the following important differences:

```text
BFS
→ Good for shortest path in unweighted environments.

DFS
→ Can be fast but may produce poor-quality paths.

UCS
→ Good when movement costs vary.

A*
→ Uses domain knowledge through a heuristic to guide the search.
```

The performance graph allows these differences to be observed rather than simply stated theoretically.

---

# 13. Limitations

Despite demonstrating several classical AI techniques, the project has some limitations.

## 13.1 Static Environment

The current maze remains unchanged while an algorithm is running.

Real-world environments may contain moving obstacles or changing terrain.

---

## 13.2 Limited Movement

The robot is restricted to four directions:

```text
UP
DOWN
LEFT
RIGHT
```

Real robots can have more complex movement models, including diagonal movement and continuous motion.

---

## 13.3 Simplified Terrain Model

Terrain costs such as:

```text
Normal = 1
Mud = 3
Water = 5
```

are simplified representations and do not model real physical movement accurately.

---

## 13.4 Grid-Based Environment

The real world is continuous, while this project represents the environment using discrete grid cells.

This simplifies the problem but does not capture all real-world navigation challenges.

---

## 13.5 Execution Time Variability

For small mazes, the execution times of algorithms can be extremely small. Differences measured in milliseconds may vary depending on:

- computer hardware
- Python runtime
- system load
- maze size

Therefore, execution time alone should not be treated as the only performance metric.

The project also compares explored states, path length, and solution cost.

---

## 13.6 Heuristic Dependency

A* performance depends on the quality of its heuristic.

The project uses Manhattan Distance because movement is restricted to four directions.

Different environments may require different heuristic functions.

---

# 14. Future Enhancements

Possible improvements include:

- Dynamic obstacles
- Moving enemies
- Multiple robots
- Real-time obstacle detection
- Diagonal movement
- Bidirectional Search
- Greedy Best-First Search
- Iterative Deepening Search
- Hill Climbing
- Simulated Annealing
- Multiple goal locations
- Battery constraints
- Real-world map integration
- Reinforcement learning-based navigation

---

# 15. Conclusion

The **AI Maze Solving Robot** demonstrates how a real-world navigation problem can be formulated as a classical AI state-space search problem.

The project defines:

```text
Initial State → Robot's starting position

Goal State → Destination cell

State Space → Traversable maze cells

Actions → Up, Down, Left, Right

Constraints → Walls, boundaries and terrain

Cost Function → Movement cost of terrain

Heuristic → Manhattan Distance
```

Four search algorithms — **BFS, DFS, UCS, and A\*** — are implemented and evaluated using the same maze environment.

The application goes beyond simply finding a path by **visualizing the explored states and final solution**, allowing users to observe how different search strategies behave.

Performance is evaluated using:

- Execution time
- Number of explored states
- Path length
- Solution cost
- Frontier size

This makes the project both an interactive game and an educational demonstration of classical AI search algorithms.

---

# 16. Key Learning Outcomes

Through this project, we demonstrate:

- State-space representation
- Problem formulation
- Uninformed search
- Informed search
- Heuristic design
- Cost-based search
- Path reconstruction
- Search visualization
- Algorithm performance analysis
- Comparative evaluation of AI algorithms
- Integration of AI algorithms into a working application

> **The main objective is not only to find a path, but to understand how different AI search strategies explore the same problem and why their performance differs.**
