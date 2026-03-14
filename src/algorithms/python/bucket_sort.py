def bucket_sort(arr):
    """
    Bucket Sort Algorithm
    Time Complexity: O(n + k) average, O(n²) worst case
    Space Complexity: O(n + k)
    
    Bucket Sort distributes elements into buckets based on their value range,
    sorts each bucket individually, then concatenates the sorted buckets.
    
    Args:
        arr (list): The array to sort
        
    Returns:
        list: The sorted array
    """
    # Create a copy to avoid modifying the original array
    array = arr.copy()
    n = len(array)
    
    if n <= 1:
        return array
    
    # Find min and max for normalization
    min_val = min(array)
    max_val = max(array)
    value_range = max_val - min_val
    
    # Handle edge case: all elements are the same
    if value_range == 0:
        return array
    
    # Create buckets (use sqrt(n) buckets for optimal distribution)
    import math
    bucket_count = max(1, int(math.sqrt(n)))
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribute elements into buckets
    for value in array:
        # Normalize value to bucket index [0, bucket_count-1]
        bucket_index = min(
            bucket_count - 1,
            int(((value - min_val) / value_range) * bucket_count)
        )
        buckets[bucket_index].append(value)
    
    # Sort each bucket using insertion sort
    for bucket in buckets:
        if len(bucket) <= 1:
            continue
        
        # Insertion sort
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            
            bucket[j + 1] = key
    
    # Concatenate sorted buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result


# Example usage and test
if __name__ == "__main__":
    # Test with sample data
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    
    sorted_array = bucket_sort(test_array)
    print(f"Sorted array: {sorted_array}")
    
    # Test with edge cases
    print(f"Empty array: {bucket_sort([])}")
    print(f"Single element: {bucket_sort([42])}")
    print(f"Already sorted: {bucket_sort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {bucket_sort([5, 4, 3, 2, 1])}")
    print(f"Duplicates: {bucket_sort([5, 2, 8, 2, 9, 1, 5, 5])}")
    print(f"Negative numbers: {bucket_sort([-5, -2, 3, -1, 0, 10])}")


