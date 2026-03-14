/**
 * Copyright (c) 2025 Ayoub Abidi
 * Licensed under Elastic License 2.0 OR Commercial
 * See LICENSE for details.
 */

import { useTranslation } from 'react-i18next';

export const useAlgorithmConfig = () => {
  const { t } = useTranslation();

  // Sorting algorithms configuration
  const sortingAlgorithms = [
    {
      value: 'bubbleSort',
      label: t('algorithms.sorting.bubbleSort'),
      complexity: t('complexity.bubbleSort'),
    },
    {
      value: 'quickSort',
      label: t('algorithms.sorting.quickSort'),
      complexity: t('complexity.quickSort'),
    },
    {
      value: 'mergeSort',
      label: t('algorithms.sorting.mergeSort'),
      complexity: t('complexity.mergeSort'),
    },
    {
      value: 'selectionSort',
      label: t('algorithms.sorting.selectionSort'),
      complexity: t('complexity.selectionSort'),
    },
    {
      value: 'insertionSort',
      label: t('algorithms.sorting.insertionSort'),
      complexity: t('complexity.insertionSort'),
    },
    {
      value: 'heapSort',
      label: t('algorithms.sorting.heapSort'),
      complexity: t('complexity.heapSort'),
    },
    {
      value: 'shellSort',
      label: t('algorithms.sorting.shellSort'),
      complexity: t('complexity.shellSort'),
    },
    {
      value: 'radixSort',
      label: t('algorithms.sorting.radixSort'),
      complexity: t('complexity.radixSort'),
    },
    {
      value: 'countingSort',
      label: t('algorithms.sorting.countingSort'),
      complexity: t('complexity.countingSort'),
    },
    {
      value: 'bucketSort',
      label: t('algorithms.sorting.bucketSort'),
      complexity: t('complexity.bucketSort'),
    },
    {
      value: 'cycleSort',
      label: t('algorithms.sorting.cycleSort'),
      complexity: t('complexity.cycleSort'),
    },
    {
      value: 'combSort',
      label: t('algorithms.sorting.combSort'),
      complexity: t('complexity.combSort'),
    },
    {
      value: 'timSort',
      label: t('algorithms.sorting.timSort'),
      complexity: t('complexity.timSort'),
    },
    {
      value: 'bogoSort',
      label: t('algorithms.sorting.bogoSort'),
      complexity: t('complexity.bogoSort'),
    },
  ];

  // Pathfinding algorithms configuration
  const pathfindingAlgorithms = [
    {
      value: 'bfs',
      label: t('algorithms.pathfinding.bfs'),
      complexity: t('complexity.bfs'),
    },
    {
      value: 'dijkstra',
      label: t('algorithms.pathfinding.dijkstra'),
      complexity: t('complexity.dijkstra'),
    },
    {
      value: 'aStar',
      label: t('algorithms.pathfinding.aStar'),
      complexity: t('complexity.aStar'),
    },
    {
      value: 'bidirectionalSearch',
      label: t('algorithms.pathfinding.bidirectionalSearch'),
      complexity: t('complexity.bidirectionalSearch'),
    },
    {
      value: 'greedyBestFirstSearch',
      label: t('algorithms.pathfinding.greedyBestFirstSearch'),
      complexity: t('complexity.greedyBestFirstSearch'),
    },
    {
      value: 'jumpPointSearch',
      label: t('algorithms.pathfinding.jumpPointSearch'),
      complexity: t('complexity.jumpPointSearch'),
    },
    {
      value: 'bellmanFord',
      label: t('algorithms.pathfinding.bellmanFord'),
      complexity: t('complexity.bellmanFord'),
    },
    {
      value: 'idaStar',
      label: t('algorithms.pathfinding.idaStar'),
      complexity: t('complexity.idaStar'),
    },
    {
      value: 'dStarLite',
      label: t('algorithms.pathfinding.dStarLite'),
      complexity: t('complexity.dStarLite'),
    },
  ];

  // Algorithm groups for better organization
  const sortingGroups = [
    {
      label: t('algorithmGroups.comparisonBased'),
      algorithms: [
        'bubbleSort',
        'quickSort',
        'mergeSort',
        'selectionSort',
        'insertionSort',
        'heapSort',
        'shellSort',
        'combSort',
        'timSort',
      ],
    },
    {
      label: t('algorithmGroups.nonComparison'),
      algorithms: ['radixSort', 'countingSort', 'bucketSort'],
    },
    {
      label: t('algorithmGroups.writeOptimal'),
      algorithms: ['cycleSort'],
    },
    {
      label: t('algorithmGroups.educational'),
      algorithms: ['bogoSort'],
    },
  ];

  const pathfindingGroups = [
    {
      label: t('algorithmGroups.unweighted'),
      algorithms: ['bfs', 'bidirectionalSearch'],
    },
    {
      label: t('algorithmGroups.weightedOptimal'),
      algorithms: ['dijkstra', 'aStar', 'idaStar', 'dStarLite'],
    },
    {
      label: t('algorithmGroups.heuristicBased'),
      algorithms: ['greedyBestFirstSearch', 'jumpPointSearch'],
    },
    {
      label: t('algorithmGroups.specialCases'),
      algorithms: ['bellmanFord'],
    },
  ];

  return {
    sortingAlgorithms,
    pathfindingAlgorithms,
    sortingGroups,
    pathfindingGroups,
  };
};
