/**
 * Copyright (c) 2025 Ayoub Abidi
 * Licensed under Elastic License 2.0 OR Commercial
 * See LICENSE for details.
 */

import { bubbleSort, bubbleSortPure } from './sorting/bubbleSort';
import { quickSort, quickSortPure } from './sorting/quickSort';
import { mergeSort, mergeSortPure } from './sorting/mergeSort';
import { selectionSort, selectionSortPure } from './sorting/selectionSort';
import { insertionSort, insertionSortPure } from './sorting/insertionSort';
import { heapSort, heapSortPure } from './sorting/heapSort';
import { shellSort, shellSortPure } from './sorting/shellSort';
import { radixSort, radixSortPure } from './sorting/radixSort';
import { countingSort, countingSortPure } from './sorting/countingSort';
import { bucketSort, bucketSortPure } from './sorting/bucketSort';
import { cycleSort, cycleSortPure } from './sorting/cycleSort';
import { combSort, combSortPure } from './sorting/combSort';

export const algorithms = {
  bubbleSort,
  quickSort,
  mergeSort,
  selectionSort,
  insertionSort,
  heapSort,
  shellSort,
  radixSort,
  countingSort,
  bucketSort,
  cycleSort,
  combSort,
};

export const pureAlgorithms = {
  bubbleSort: bubbleSortPure,
  quickSort: quickSortPure,
  mergeSort: mergeSortPure,
  selectionSort: selectionSortPure,
  insertionSort: insertionSortPure,
  heapSort: heapSortPure,
  shellSort: shellSortPure,
  radixSort: radixSortPure,
  countingSort: countingSortPure,
  bucketSort: bucketSortPure,
  cycleSort: cycleSortPure,
  combSort: combSortPure,
};

export {
  bubbleSort,
  quickSort,
  mergeSort,
  selectionSort,
  insertionSort,
  heapSort,
  shellSort,
  radixSort,
  countingSort,
  bucketSort,
  cycleSort,
  combSort,
};
export {
  bubbleSortPure,
  quickSortPure,
  mergeSortPure,
  selectionSortPure,
  insertionSortPure,
  heapSortPure,
  shellSortPure,
  radixSortPure,
  countingSortPure,
  bucketSortPure,
  cycleSortPure,
  combSortPure,
};
