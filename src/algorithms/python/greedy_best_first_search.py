"""
Greedy Best-First Search Pathfinding Algorithm

Greedy Best-First Search uses heuristics to guide its search towards the goal.
Unlike A*, it only considers the heuristic distance h(n) and ignores the path cost g(n).
This makes it faster but doesn't guarantee the shortest path.

Time Complexity: O(b^d) where b is branching factor and d is depth
Space Complexity: O(b^d)
"""

import heapq


def manhattan_distance(a, b):
    """
    Calculate Manhattan distance between two points.
    
    Args:
        a (tuple): First point (row, col)
        b (tuple): Second point (row, col)
    
    Returns:
        int: Manhattan distance
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first_search(grid, start, end):
    """
    Greedy Best-First Search pathfinding algorithm.
    
    Args:
        grid (list): 2D grid (not used for pathfinding, but kept for consistency)
        start (tuple): Starting position (row, col)
        end (tuple): Ending position (row, col)
    
    Returns:
        list: Path from start to end, or None if no path exists
    """
    if not start or not end:
        return None
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Check bounds
    if (start[0] < 0 or start[0] >= rows or 
        start[1] < 0 or start[1] >= cols or
        end[0] < 0 or end[0] >= rows or 
        end[1] < 0 or end[1] >= cols):
        return None
    
    # Check if start and end are the same
    if start == end:
        return [start]
    
    # Priority queue based on heuristic distance to goal
    # Each element: (heuristic, row, col)
    open_set = [(manhattan_distance(start, end), start[0], start[1])]
    heapq.heapify(open_set)
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    
    visited[start[0]][start[1]] = True
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_set:
        h, row, col = heapq.heappop(open_set)
        
        # Check if we reached the goal
        if (row, col) == end:
            # Reconstruct path
            path = []
            current = end
            while current != start:
                path.append(current)
                current = parent[current[0]][current[1]]
            path.append(start)
            path.reverse()
            return path
        
        # Explore neighbors
        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            
            # Check bounds
            if (0 <= new_row < rows and 0 <= new_col < cols and
                not visited[new_row][new_col]):
                
                visited[new_row][new_col] = True
                parent[new_row][new_col] = (row, col)
                
                # Add to open set with heuristic as priority
                heuristic = manhattan_distance((new_row, new_col), end)
                heapq.heappush(open_set, (heuristic, new_row, new_col))
    
    # No path found
    return None


# Example usage and testing
if __name__ == "__main__":
    # Example grid (5x5)
    grid = [[0 for _ in range(5)] for _ in range(5)]
    start = (0, 0)
    end = (4, 4)
    
    print("Greedy Best-First Search Pathfinding")
    print(f"Start: {start}")
    print(f"End: {end}")
    print(f"Grid size: {len(grid)}x{len(grid[0])}")
    print()
    
    path = greedy_best_first_search(grid, start, end)
    
    if path:
        print(f"Path found! Length: {len(path)} cells")
        print("Path:")
        for i, (row, col) in enumerate(path):
            print(f"  {i+1}. ({row}, {col})")
    else:
        print("No path found!")
    
    print()
    print("Note: Greedy Best-First Search may not find the shortest path,")
    print("but it's often faster than optimal algorithms like A*.")


