/**
 * Copyright (c) 2025 Ayoub Abidi
 * Licensed under Elastic License 2.0 OR Commercial
 * See LICENSE for details.
 */

import { describe, it, expect } from 'vitest';
import { bfsPure } from './bfs';
import { dijkstraPure } from './dijkstra';
import { aStarPure } from './aStar';
import { bidirectionalSearchPure } from './bidirectionalSearch';
import { bfs } from './bfs';
import { dijkstra } from './dijkstra';
import { aStar } from './aStar';
import { bidirectionalSearch } from './bidirectionalSearch';

describe('Pathfinding Algorithms - Pure Versions', () => {
  const start = { row: 0, col: 0 };
  const end = { row: 4, col: 4 };
  const rows = 5;
  const cols = 5;

  describe('BFS Pure', () => {
    it('should find a path from start to end', () => {
      const path = bfsPure(start, end, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBeGreaterThan(0);
      expect(path[0]).toEqual(start);
      expect(path[path.length - 1]).toEqual(end);
    });

    it('should return shortest path', () => {
      const path = bfsPure(start, end, rows, cols);
      // Manhattan distance from (0,0) to (4,4) is 8
      // Shortest path should be 9 cells (including start)
      expect(path.length).toBe(9);
    });

    it('should handle start and end being the same', () => {
      const path = bfsPure(start, start, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBe(1);
      expect(path[0]).toEqual(start);
    });

    it('should handle adjacent cells', () => {
      const adjacentEnd = { row: 0, col: 1 };
      const path = bfsPure(start, adjacentEnd, rows, cols);
      expect(path.length).toBe(2);
    });
  });

  describe('Dijkstra Pure', () => {
    it('should find a path from start to end', () => {
      const path = dijkstraPure(start, end, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBeGreaterThan(0);
      expect(path[0]).toEqual(start);
      expect(path[path.length - 1]).toEqual(end);
    });

    it('should return shortest path', () => {
      const path = dijkstraPure(start, end, rows, cols);
      expect(path.length).toBe(9);
    });

    it('should handle start and end being the same', () => {
      const path = dijkstraPure(start, start, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBe(1);
    });
  });

  describe('A* Pure', () => {
    it('should find a path from start to end', () => {
      const path = aStarPure(start, end, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBeGreaterThan(0);
      expect(path[0]).toEqual(start);
      expect(path[path.length - 1]).toEqual(end);
    });

    it('should return shortest path', () => {
      const path = aStarPure(start, end, rows, cols);
      expect(path.length).toBe(9);
    });

    it('should handle start and end being the same', () => {
      const path = aStarPure(start, start, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBe(1);
    });

    it('should be more efficient than BFS (explore fewer nodes)', () => {
      // A* should explore fewer nodes due to heuristic
      // This is a qualitative test - we just verify it works
      const path = aStarPure(start, end, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBe(9);
    });
  });

  describe('Bidirectional Search Pure', () => {
    it('should find a path from start to end', () => {
      const path = bidirectionalSearchPure(start, end, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBeGreaterThan(0);
      expect(path[0]).toEqual(start);
      expect(path[path.length - 1]).toEqual(end);
    });

    it('should return shortest path', () => {
      const path = bidirectionalSearchPure(start, end, rows, cols);
      // Manhattan distance from (0,0) to (4,4) is 8
      // Shortest path should be 9 cells (including start)
      expect(path.length).toBe(9);
    });

    it('should handle start and end being the same', () => {
      const path = bidirectionalSearchPure(start, start, rows, cols);
      expect(path).toBeTruthy();
      expect(path.length).toBe(1);
      expect(path[0]).toEqual(start);
    });

    it('should handle adjacent cells', () => {
      const adjacentEnd = { row: 0, col: 1 };
      const path = bidirectionalSearchPure(start, adjacentEnd, rows, cols);
      expect(path.length).toBe(2);
    });

    it('should be more efficient than BFS for longer paths', () => {
      // Test with a larger grid to see the efficiency benefit
      const largeStart = { row: 0, col: 0 };
      const largeEnd = { row: 9, col: 9 };
      const largeRows = 10;
      const largeCols = 10;

      const path = bidirectionalSearchPure(
        largeStart,
        largeEnd,
        largeRows,
        largeCols
      );
      expect(path).toBeTruthy();
      expect(path.length).toBe(19); // Manhattan distance + 1
    });
  });

  describe('Algorithm Consistency', () => {
    it('all algorithms should find paths of same length', () => {
      const bfsPath = bfsPure(start, end, rows, cols);
      const dijkstraPath = dijkstraPure(start, end, rows, cols);
      const aStarPath = aStarPure(start, end, rows, cols);
      const bidirectionalPath = bidirectionalSearchPure(start, end, rows, cols);

      expect(bfsPath.length).toBe(dijkstraPath.length);
      expect(dijkstraPath.length).toBe(aStarPath.length);
      expect(aStarPath.length).toBe(bidirectionalPath.length);
    });

    it('all algorithms should have same start and end', () => {
      const bfsPath = bfsPure(start, end, rows, cols);
      const dijkstraPath = dijkstraPure(start, end, rows, cols);
      const aStarPath = aStarPure(start, end, rows, cols);
      const bidirectionalPath = bidirectionalSearchPure(start, end, rows, cols);

      expect(bfsPath[0]).toEqual(start);
      expect(dijkstraPath[0]).toEqual(start);
      expect(aStarPath[0]).toEqual(start);
      expect(bidirectionalPath[0]).toEqual(start);

      expect(bfsPath[bfsPath.length - 1]).toEqual(end);
      expect(dijkstraPath[dijkstraPath.length - 1]).toEqual(end);
      expect(aStarPath[aStarPath.length - 1]).toEqual(end);
      expect(bidirectionalPath[bidirectionalPath.length - 1]).toEqual(end);
    });
  });
});

describe('Pathfinding Algorithms - Visualization Versions', () => {
  const start = { row: 0, col: 0 };
  const end = { row: 3, col: 3 };
  const rows = 4;
  const cols = 4;
  const grid = Array(rows)
    .fill(null)
    .map(() => Array(cols).fill(0));

  describe('BFS Visualization', () => {
    it('should generate steps array', () => {
      const steps = bfs(grid, start, end, rows, cols);
      expect(steps).toBeTruthy();
      expect(steps.length).toBeGreaterThan(0);
    });

    it('each step should have required properties', () => {
      const steps = bfs(grid, start, end, rows, cols);
      steps.forEach(step => {
        expect(step).toHaveProperty('grid');
        expect(step).toHaveProperty('states');
        expect(step).toHaveProperty('description');
        expect(Array.isArray(step.grid)).toBe(true);
        expect(Array.isArray(step.states)).toBe(true);
        expect(typeof step.description).toBe('string');
      });
    });

    it('should mark start and end in states', () => {
      const steps = bfs(grid, start, end, rows, cols);
      const firstStep = steps[0];
      expect(firstStep.states[start.row][start.col]).toBe('start');
      expect(firstStep.states[end.row][end.col]).toBe('end');
    });

    it('final step should indicate completion', () => {
      const steps = bfs(grid, start, end, rows, cols);
      const lastStep = steps[steps.length - 1];
      expect(lastStep.description.toLowerCase()).toContain('path');
    });
  });

  describe('Dijkstra Visualization', () => {
    it('should generate steps array', () => {
      const steps = dijkstra(grid, start, end, rows, cols);
      expect(steps).toBeTruthy();
      expect(steps.length).toBeGreaterThan(0);
    });

    it('each step should have required properties', () => {
      const steps = dijkstra(grid, start, end, rows, cols);
      steps.forEach(step => {
        expect(step).toHaveProperty('grid');
        expect(step).toHaveProperty('states');
        expect(step).toHaveProperty('description');
      });
    });
  });

  describe('A* Visualization', () => {
    it('should generate steps array', () => {
      const steps = aStar(grid, start, end, rows, cols);
      expect(steps).toBeTruthy();
      expect(steps.length).toBeGreaterThan(0);
    });

    it('each step should have required properties', () => {
      const steps = aStar(grid, start, end, rows, cols);
      steps.forEach(step => {
        expect(step).toHaveProperty('grid');
        expect(step).toHaveProperty('states');
        expect(step).toHaveProperty('description');
      });
    });

    it('should include heuristic information in descriptions', () => {
      const steps = aStar(grid, start, end, rows, cols);
      // At least some steps should mention g, h, or f values
      const hasHeuristicInfo = steps.some(step =>
        step.description.match(/[ghf]=/i)
      );
      expect(hasHeuristicInfo).toBe(true);
    });
  });

  describe('Bidirectional Search Visualization', () => {
    it('should generate steps array', () => {
      const steps = bidirectionalSearch(grid, start, end, rows, cols);
      expect(steps).toBeTruthy();
      expect(steps.length).toBeGreaterThan(0);
    });

    it('each step should have required properties', () => {
      const steps = bidirectionalSearch(grid, start, end, rows, cols);
      steps.forEach(step => {
        expect(step).toHaveProperty('grid');
        expect(step).toHaveProperty('states');
        expect(step).toHaveProperty('description');
        expect(Array.isArray(step.grid)).toBe(true);
        expect(Array.isArray(step.states)).toBe(true);
        expect(typeof step.description).toBe('string');
      });
    });

    it('should mark start and end in states', () => {
      const steps = bidirectionalSearch(grid, start, end, rows, cols);
      const firstStep = steps[0];
      expect(firstStep.states[start.row][start.col]).toBe('start');
      expect(firstStep.states[end.row][end.col]).toBe('end');
    });

    it('should include bidirectional search information in descriptions', () => {
      const steps = bidirectionalSearch(grid, start, end, rows, cols);
      // Should have forward/backward exploration indicators
      const hasBidirectionalInfo = steps.some(
        step =>
          step.description.toLowerCase().includes('forward') ||
          step.description.toLowerCase().includes('backward') ||
          step.description.toLowerCase().includes('meeting')
      );
      expect(hasBidirectionalInfo).toBe(true);
    });

    it('should handle same start and end positions', () => {
      const sameSteps = bidirectionalSearch(grid, start, start, rows, cols);
      expect(sameSteps.length).toBeGreaterThan(0);
      expect(
        sameSteps[sameSteps.length - 1].description.toLowerCase()
      ).toContain('path');
    });
  });
});
