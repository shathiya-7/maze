import React, { useState, useEffect } from "react";
import MazeCell from "./MazeCell";
import { CELL_TYPES } from "../utils/constants";

const MazeGrid = ({ grid, robotPos, visualState, onReset }) => {
  const columnCount = grid[0]?.length ?? 0;

  return (
    <div 
      className="grid gap-1 p-4 bg-slate-900 rounded-xl shadow-2xl border border-slate-700"
      style={{ 
        gridTemplateColumns: `repeat(${columnCount || 1}, minmax(0, 1fr))`,
        width: "fit-content",
        margin: "0 auto"
      }}
    >
      {grid.map((row, r) => 
        row.map((cell, c) => {
          let type = cell;
          if (visualState[r]?.[c]) {
            type = visualState[r][c];
          }
          return (
            <div key={`${r}-${c}`} className="w-6 h-6 sm:w-8 sm:h-8">
              <MazeCell 
                type={type} 
                isRobot={robotPos && robotPos[0] === r && robotPos[1] === c} 
              />
            </div>
          );
        })
      )}
    </div>
  );
};

export default MazeGrid;
