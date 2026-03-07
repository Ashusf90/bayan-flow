def counting_sort(arr):
    """
    Counting Sort Algorithm
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(n + k)
    
    Counting Sort is a non-comparison sorting algorithm that works by counting
    the number of objects having distinct key values, then doing arithmetic to
    calculate the position of each object in the output sequence.
    
    Note: This implementation only works with non-negative integers.
    
    Args:
        arr (list): The array to sort (non-negative integers only)
        
    Returns:
        list: The sorted array
    """
    # Create a copy to avoid modifying the original array
    array = arr.copy()
    n = len(array)
    
    if n == 0:
        return array
    
    # Find the maximum value to determine counting array size
    max_val = max(array)
    
    # Initialize counting array
    count = [0] * (max_val + 1)
    
    # Count occurrences of each element
    for num in array:
        count[num] += 1
    
    # Modify count array to contain actual positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build the output array (iterate backwards for stability)
    output = [0] * n
    for i in range(n - 1, -1, -1):
        value = array[i]
        position = count[value] - 1
        output[position] = value
        count[value] -= 1
    
    return output


# Example usage and test
if __name__ == "__main__":
    # Test with sample data
    test_array = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original array: {test_array}")
    
    sorted_array = counting_sort(test_array)
    print(f"Sorted array: {sorted_array}")
    
    # Test with edge cases
    print(f"Empty array: {counting_sort([])}")
    print(f"Single element: {counting_sort([42])}")
    print(f"Already sorted: {counting_sort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {counting_sort([5, 4, 3, 2, 1])}")
    print(f"Duplicates: {counting_sort([5, 2, 8, 2, 9, 1, 5, 5])}")
    print(f"All same: {counting_sort([3, 3, 3, 3, 3])}")


