"""
Tim Sort Algorithm
Time Complexity: O(n log n)
Space Complexity: O(n)

Tim Sort is a hybrid stable sorting algorithm derived from merge sort and insertion sort.
It is the default sorting algorithm in Python, Java, Swift, and Android.
This is a simplified educational version.
"""

MIN_MERGE = 32


def insertion_sort(arr, left, right):
    """Sort a run using insertion sort."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    """Merge two sorted runs."""
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def tim_sort(arr):
    """
    Tim Sort implementation.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    n = len(arr)
    min_run = min(MIN_MERGE, n)
    
    # Sort individual runs using insertion sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    
    # Merge runs
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            
            if mid < end:
                merge(arr, start, mid, end)
        
        size *= 2
    
    return arr


# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 18, 77]
    print("Original array:", arr)
    
    sorted_arr = tim_sort(arr.copy())
    print("Sorted array:", sorted_arr)
