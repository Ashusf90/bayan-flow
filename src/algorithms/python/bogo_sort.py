import random


def bogo_sort(arr, max_attempts=1000):
    """
    Bogo Sort Algorithm (Permutation Sort)
    Time Complexity: O(n × n!) average, Unbounded worst case
    Space Complexity: O(1)
    
    Bogo Sort repeatedly randomly shuffles the array until it happens to be sorted.
    It is intentionally inefficient and mainly used for educational purposes.
    
    Args:
        arr (list): The array to sort
        max_attempts (int): Maximum shuffle attempts to prevent infinite loops
        
    Returns:
        list: The sorted array (or partially sorted if max_attempts reached)
    """
    # Create a copy to avoid modifying the original array
    array = arr.copy()
    attempts = 0
    
    def is_sorted(arr):
        """Check if array is sorted"""
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    
    # Keep shuffling until sorted or max attempts reached
    while not is_sorted(array) and attempts < max_attempts:
        random.shuffle(array)
        attempts += 1
    
    return array


# Example usage and test
if __name__ == "__main__":
    # Test with small arrays only (due to factorial complexity)
    test_array = [3, 1, 2]
    print(f"Original array: {test_array}")
    
    sorted_array = bogo_sort(test_array)
    print(f"Sorted array: {sorted_array}")
    print(f"Is sorted: {sorted_array == sorted(test_array)}")
    
    # Test with edge cases
    print(f"Empty array: {bogo_sort([])}")
    print(f"Single element: {bogo_sort([42])}")
    print(f"Already sorted: {bogo_sort([1, 2, 3])}")
    
    # Warning: Do not test with large arrays!
    print("\n⚠️  Warning: Bogo Sort has O(n × n!) complexity.")
    print("Never use this algorithm in production!")
