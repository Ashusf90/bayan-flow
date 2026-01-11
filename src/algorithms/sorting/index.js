import { bubbleSort, bubbleSortPure } from './bubbleSort';
import { quickSort, quickSortPure } from './quickSort';
import { mergeSort, mergeSortPure } from './mergeSort';
import { selectionSort, selectionSortPure } from './selectionSort';
import { insertionSort, insertionSortPure } from './insertionSort';
import { heapSort, heapSortPure } from './heapSort';
import { shellSort, shellSortPure } from './shellSort';
import { radixSort, radixSortPure } from './radixSort';
import { countingSort, countingSortPure } from './countingSort';

export const sortingAlgorithms = {
  bubbleSort,
  quickSort,
  mergeSort,
  selectionSort,
  insertionSort,
  heapSort,
  shellSort,
  radixSort,
  countingSort,
};

export const pureSortingAlgorithms = {
  bubbleSort: bubbleSortPure,
  quickSort: quickSortPure,
  mergeSort: mergeSortPure,
  selectionSort: selectionSortPure,
  insertionSort: insertionSortPure,
  heapSort: heapSortPure,
  shellSort: shellSortPure,
  radixSort: radixSortPure,
  countingSort: countingSortPure,
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
};
