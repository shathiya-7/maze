import axios from "axios";
import { API_BASE } from "../utils/constants";

const api = axios.create({
  baseURL: API_BASE,
});

export const mazeService = {
  generateMaze: async (rows = 21, cols = 21, density = 0.2) => {
    const response = await api.post(`/api/maze/generate?rows=${rows}&cols=${cols}&density=${density}`);
    return response.data;
  },
  solveMaze: async (payload) => {
    const response = await api.post("/api/solve", payload);
    return response.data;
  },
  compareAlgorithms: async (payload) => {
    const response = await api.post("/api/compare", payload);
    return response.data;
  }
};
