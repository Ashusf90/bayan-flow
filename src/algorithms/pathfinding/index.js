/**
 * Copyright (c) 2025 Ayoub Abidi
 * Licensed under Elastic License 2.0 OR Commercial
 * See LICENSE for details.
 */

import { bfs, bfsPure } from './bfs';
import { dijkstra, dijkstraPure } from './dijkstra';
import { aStar, aStarPure } from './aStar';
import {
  bidirectionalSearch,
  bidirectionalSearchPure,
} from './bidirectionalSearch';

export const pathfindingAlgorithms = {
  bfs,
  dijkstra,
  aStar,
  bidirectionalSearch,
};

export const purePathfindingAlgorithms = {
  bfs: bfsPure,
  dijkstra: dijkstraPure,
  aStar: aStarPure,
  bidirectionalSearch: bidirectionalSearchPure,
};

export { bfs, dijkstra, aStar, bidirectionalSearch };
export { bfsPure, dijkstraPure, aStarPure, bidirectionalSearchPure };
