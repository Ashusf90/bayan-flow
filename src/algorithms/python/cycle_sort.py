def cycle_sort(arr):
    """
    Cycle Sort Algorithm
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Cycle Sort minimizes the number of memory writes by placing each element
    directly into its final sorted position. It performs at most n-1 writes,
    making it optimal for situations where write operations are expensive.
    
    Args:
        arr (list): The array to sort
        
    Returns:
        list: The sorted array
    """
    # Create a copy to avoid modifying the original array
    array = arr.copy()
    n = len(array)
    
    # Traverse the array to find cycles
    for cycle_start in range(n - 1):
        # Initialize item as starting point
        item = array[cycle_start]
        
        # Find position where we put the item
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if array[i] < item:
                pos += 1
        
        # If item is already in correct position
        if pos == cycle_start:
            continue
        
        # Skip duplicates
        while item == array[pos]:
            pos += 1
        
        # Put the item to its correct position
        if pos != cycle_start:
            item, array[pos] = array[pos], item
        
        # Rotate rest of the cycle
        while pos != cycle_start:
            pos = cycle_start
            
            # Find position where we put the element
            for i in range(cycle_start + 1, n):
                if array[i] < item:
                    pos += 1
            
            # Skip duplicates
            while item == array[pos]:
                pos += 1
            
            # Put the item to its correct position
            if item != array[pos]:
                item, array[pos] = array[pos], item
    
    return array


# Example usage and test
if __name__ == "__main__":
    # Test with sample data
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    
    sorted_array = cycle_sort(test_array)
    print(f"Sorted array: {sorted_array}")
    
    # Test with edge cases
    print(f"Empty array: {cycle_sort([])}")
    print(f"Single element: {cycle_sort([42])}")
    print(f"Already sorted: {cycle_sort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {cycle_sort([5, 4, 3, 2, 1])}")
    print(f"With duplicates: {cycle_sort([5, 2, 8, 2, 9, 1, 5, 5])}")
