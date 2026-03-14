/**
 * Copyright (c) 2025 Ayoub Abidi
 * Licensed under Elastic License 2.0 OR Commercial
 * See LICENSE for details.
 */

import { describe, it, expect } from 'vitest';
import { renderHook } from '@testing-library/react';
import { I18nextProvider } from 'react-i18next';
import i18n from '../i18n';
import { useAlgorithmConfig } from './algorithmConfig';

const wrapper = ({ children }) => (
  <I18nextProvider i18n={i18n}>{children}</I18nextProvider>
);

describe('useAlgorithmConfig', () => {
  it('should return sortingAlgorithms array with 14 items', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    expect(result.current.sortingAlgorithms).toBeDefined();
    expect(Array.isArray(result.current.sortingAlgorithms)).toBe(true);
    expect(result.current.sortingAlgorithms).toHaveLength(14);
  });

  it('each sorting algorithm should have value, label, complexity', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    result.current.sortingAlgorithms.forEach(algo => {
      expect(algo).toHaveProperty('value');
      expect(algo).toHaveProperty('label');
      expect(algo).toHaveProperty('complexity');
      expect(typeof algo.value).toBe('string');
      expect(typeof algo.label).toBe('string');
      expect(typeof algo.complexity).toBe('string');
    });
  });

  it('should return pathfindingAlgorithms array with 9 items', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    expect(result.current.pathfindingAlgorithms).toBeDefined();
    expect(Array.isArray(result.current.pathfindingAlgorithms)).toBe(true);
    expect(result.current.pathfindingAlgorithms).toHaveLength(9);
  });

  it('each pathfinding algorithm should have value, label, complexity', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    result.current.pathfindingAlgorithms.forEach(algo => {
      expect(algo).toHaveProperty('value');
      expect(algo).toHaveProperty('label');
      expect(algo).toHaveProperty('complexity');
    });
  });

  it('should return sortingGroups array with 4 groups', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    expect(result.current.sortingGroups).toBeDefined();
    expect(Array.isArray(result.current.sortingGroups)).toBe(true);
    expect(result.current.sortingGroups).toHaveLength(4);
  });

  it('each sorting group should have label and algorithms', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    result.current.sortingGroups.forEach(group => {
      expect(group).toHaveProperty('label');
      expect(group).toHaveProperty('algorithms');
      expect(Array.isArray(group.algorithms)).toBe(true);
    });
  });

  it('should return pathfindingGroups array with 4 groups', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    expect(result.current.pathfindingGroups).toBeDefined();
    expect(Array.isArray(result.current.pathfindingGroups)).toBe(true);
    expect(result.current.pathfindingGroups).toHaveLength(4);
  });

  it('each pathfinding group should have label and algorithms', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    result.current.pathfindingGroups.forEach(group => {
      expect(group).toHaveProperty('label');
      expect(group).toHaveProperty('algorithms');
      expect(Array.isArray(group.algorithms)).toBe(true);
    });
  });

  it('should use translated labels for sorting algorithms', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    const bubbleSort = result.current.sortingAlgorithms.find(
      a => a.value === 'bubbleSort'
    );
    expect(bubbleSort).toBeDefined();
    expect(bubbleSort.label).toBeTruthy();
    expect(i18n.t('algorithms.sorting.bubbleSort')).toBe(bubbleSort.label);
  });

  it('should use translated labels for pathfinding algorithms', () => {
    const { result } = renderHook(() => useAlgorithmConfig(), { wrapper });

    const bfs = result.current.pathfindingAlgorithms.find(
      a => a.value === 'bfs'
    );
    expect(bfs).toBeDefined();
    expect(bfs.label).toBeTruthy();
    expect(i18n.t('algorithms.pathfinding.bfs')).toBe(bfs.label);
  });
});
