import React, { useState, useEffect } from "react";
import { mazeService } from "../services/api";
import MazeGrid from "../components/MazeGrid";
import { ALGORITHMS, CELL_TYPES } from "../utils/constants";

const Game = () => {
  const [grid, setGrid] = useState([]);
  const [robotPos, setRobotPos] = useState(null);
  const [visualState, setVisualState] = useState({});
  const [algo, setAlgo] = useState("BFS");
  const [status, setStatus] = useState("IDLE"); // IDLE, SEARCHING, FOUND, PATHING
  const [metrics, setMetrics] = useState({ nodes: 0, cost: 0, time: 0 });
  const [speed, setSpeed] = useState(50);

  const generate = async () => {
    const data = await mazeService.generateMaze();
    setGrid(data.grid);
    setVisualState({});
    setRobotPos([0, 0]);
    setStatus("IDLE");
  };

  useEffect(() => { generate(); }, []);

  const runAI = async () => {
    if (!grid.length || !grid[0]?.length) {
      return;
    }

    setStatus("SEARCHING");
    const start = [0, 0];
    const goal = [grid.length - 1, grid[0].length - 1];

    const result = await mazeService.solveMaze({
      algorithm: algo,
      grid: grid,
      start: start,
      goal: goal
    });

    if (result.path.length === 0) {
      setStatus("FAILED");
      return;
    }

    // Replay events for visualization
    let currentVisuals = {};
    for (const event of result.events) {
      const [r, c] = event.cell;
      if (event.type === "explore") currentVisuals[r] = { ...currentVisuals[r], [c]: CELL_TYPES.EXPLORED };
      if (event.type === "discover") currentVisuals[r] = { ...currentVisuals[r], [c]: CELL_TYPES.FRONTIER };
      if (event.type === "start") setRobotPos([r, c]);
      
      setVisualState({ ...currentVisuals });
      await new Promise(resolve => setTimeout(resolve, 101 - speed));
    }

    setStatus("FOUND");
    setMetrics({
      nodes: result.nodes_explored,
      cost: result.cost,
      time: result.execution_time
    });

    // Animate final path
    for (const cell of result.path) {
      const [r, c] = cell;
      setRobotPos([r, c]);
      setVisualState(prev => {
        const newState = { ...prev };
        newState[r] = { ...newState[r], [c]: CELL_TYPES.PATH };
        return newState;
      });
      await new Promise(resolve => setTimeout(resolve, 101 - speed));
    }
    setStatus("SUCCESS");
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-8 font-mono">
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <div className="lg:col-span-2 flex flex-col items-center gap-6">
          <h1 className="text-4xl font-bold tracking-tighter text-cyan-400">AI MAZE LABORATORY</h1>
          <MazeGrid grid={grid} robotPos={robotPos} visualState={visualState} />
          
          <div className="flex gap-4 bg-slate-900 p-4 rounded-xl border border-slate-800 w-full justify-center">
            <select 
              className="bg-slate-800 p-2 rounded border border-slate-700 text-white"
              value={algo} 
              onChange={(e) => setAlgo(e.target.value)}
            >
              {Object.values(ALGORITHMS).map(a => <option key={a} value={a}>{a}</option>)}
            </select>
            
            <div className="flex items-center gap-2">
              <span>Speed</span>
              <input type="range" min="1" max="100" value={speed} onChange={(e) => setSpeed(Number(e.target.value))} />
            </div>

            <button 
              onClick={runAI} 
              disabled={status === "SEARCHING"}
              className="bg-cyan-600 hover:bg-cyan-500 px-6 py-2 rounded font-bold transition-colors disabled:opacity-50"
            >
              START AI
            </button>
            <button onClick={generate} className="bg-slate-700 hover:bg-slate-600 px-6 py-2 rounded font-bold transition-colors">
              RESET
            </button>
          </div>
        </div>

        <div className="bg-slate-900 p-6 rounded-xl border border-slate-800 h-fit">
          <h2 className="text-xl font-bold mb-4 text-cyan-400 border-b border-slate-800 pb-2">MISSION STATUS</h2>
          <div className="space-y-4">
            <div className="flex justify-between"><span>Algorithm:</span><span className="text-cyan-300">{algo}</span></div>
            <div className="flex justify-between"><span>Status:</span><span className="text-cyan-300">{status}</span></div>
            <div className="flex justify-between"><span>Explored:</span><span className="text-cyan-300">{metrics.nodes} cells</span></div>
            <div className="flex justify-between"><span>Path Cost:</span><span className="text-cyan-300">{metrics.cost}</span></div>
            <div className="flex justify-between"><span>Execution:</span><span className="text-cyan-300">{metrics.time.toFixed(4)}s</span></div>
          </div>
          <div className="mt-8 p-4 bg-slate-800 rounded-lg text-sm text-slate-400 italic">
            {algo === "BFS" && "Exploring level by level. Guarantees shortest path in unweighted mazes."}
            {algo === "DFS" && "Exploring as deep as possible. Not guaranteed to be shortest."}
            {algo === "UCS" && "Finding the lowest-cost path. Ideal for weighted terrain."}
            {algo === "A*" && "Using Manhattan distance to guide the search efficiently."}
          </div>
        </div>

      </div>
    </div>
  );
};

export default Game;
