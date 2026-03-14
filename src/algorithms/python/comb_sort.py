def comb_sort(arr):
    """
    Comb Sort Algorithm
    Time Complexity: O(n²) worst case, O(n log n) best case
    Space Complexity: O(1)
    
    Comb Sort improves on Bubble Sort by comparing elements separated by a shrinking gap.
    The gap shrinks by a factor of 1.3 each iteration until it reaches 1.
    This helps eliminate small values near the end of the array ("turtles") faster than Bubble Sort.
    
    Args:
        arr (list): The array to sort
        
    Returns:
        list: The sorted array
    """
    array = arr.copy()
    n = len(array)
    shrink_factor = 1.3
    
    gap = n
    swapped = True
    
    while gap > 1 or swapped:
        # Update gap for next comb
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1
        
        swapped = False
        
        # Compare all elements with current gap
        for i in range(n - gap):
            # Swap if elements are in wrong order
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
    
    return array


# Example usage and test
if __name__ == "__main__":
    # Test with sample data
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    
    sorted_array = comb_sort(test_array)
    print(f"Sorted array: {sorted_array}")
    
    # Test with edge cases
    print(f"Empty array: {comb_sort([])}")
    print(f"Single element: {comb_sort([42])}")
    print(f"Already sorted: {comb_sort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {comb_sort([5, 4, 3, 2, 1])}")
