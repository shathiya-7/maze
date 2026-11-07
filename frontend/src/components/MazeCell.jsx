import React from "react";
import { CELL_TYPES } from "../utils/constants";

const MazeCell = ({ type, isRobot, isGoal }) => {
  const baseStyle = "w-full h-full transition-all duration-300 rounded-sm";
  
  const typeStyles = {
    [CELL_TYPES.WALL]: "bg-slate-800 shadow-inner",
    [CELL_TYPES.EMPTY]: "bg-slate-700/50",
    [CELL_TYPES.START]: "bg-emerald-500 shadow-[0_0_10px_#10b981]",
    [CELL_TYPES.GOAL]: "bg-rose-500 shadow-[0_0_10px_#f43f5e] animate-pulse",
    [CELL_TYPES.MUD]: "bg-yellow-900/70",
    [CELL_TYPES.WATER]: "bg-blue-900/70",
    [CELL_TYPES.FRONTIER]: "bg-cyan-400/40",
    [CELL_TYPES.EXPLORED]: "bg-cyan-600/30",
    [CELL_TYPES.CURRENT]: "bg-white shadow-[0_0_15px_white] scale-90",
    [CELL_TYPES.PATH]: "bg-yellow-400 shadow-[0_0_8px_#facc15]",
  };

  return (
    <div className={`relative ${baseStyle} ${typeStyles[type] || typeStyles[CELL_TYPES.EMPTY]}`}>
      {isRobot && (
        <div className="absolute inset-0 flex items-center justify-center text-lg z-10 animate-bounce">
          🤖
        </div>
      )}
    </div>
  );
};

export default MazeCell;
