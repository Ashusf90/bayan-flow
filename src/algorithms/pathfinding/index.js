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
import {
  greedyBestFirstSearch,
  greedyBestFirstSearchPure,
} from './greedyBestFirstSearch';
import { jumpPointSearch, jumpPointSearchPure } from './jumpPointSearch';
import { bellmanFord, bellmanFordPure } from './bellmanFord';

export const pathfindingAlgorithms = {
  bfs,
  dijkstra,
  aStar,
  bidirectionalSearch,
  greedyBestFirstSearch,
  jumpPointSearch,
  bellmanFord,
};

export const purePathfindingAlgorithms = {
  bfs: bfsPure,
  dijkstra: dijkstraPure,
  aStar: aStarPure,
  bidirectionalSearch: bidirectionalSearchPure,
  greedyBestFirstSearch: greedyBestFirstSearchPure,
  jumpPointSearch: jumpPointSearchPure,
  bellmanFord: bellmanFordPure,
};

export {
  bfs,
  dijkstra,
  aStar,
  bidirectionalSearch,
  greedyBestFirstSearch,
  jumpPointSearch,
  bellmanFord,
};
export {
  bfsPure,
  dijkstraPure,
  aStarPure,
  bidirectionalSearchPure,
  greedyBestFirstSearchPure,
  jumpPointSearchPure,
  bellmanFordPure,
};
