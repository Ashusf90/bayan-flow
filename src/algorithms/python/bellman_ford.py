def bellman_ford(grid, start, end):
    """
    Bellman-Ford Algorithm for Pathfinding
    Time Complexity: O(VE) where V is vertices and E is edges
    Space Complexity: O(V)
    
    Single-source shortest path algorithm using iterative relaxation.
    Can handle negative edge weights and detect negative cycles.
    Runs V-1 iterations, relaxing all edges in each iteration.
    
    Args:
        grid (list): 2D grid representing the map (0 = walkable, 1 = wall)
        start (tuple): Starting position (row, col)
        end (tuple): Target position (row, col)
        
    Returns:
        list: Path from start to end as list of (row, col) tuples, or None if no path exists
    """
    rows, cols = len(grid), len(grid[0])
    
    # Initialize distances: Infinity for all cells except start
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    
    # Parent tracking for path reconstruction
    came_from = {}
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Bellman-Ford: V-1 iterations (V = rows * cols)
    max_iterations = rows * cols - 1
    
    for iteration in range(1, max_iterations + 1):
        updated = False
        
        # Relax all edges in this iteration
        for row in range(rows):
            for col in range(cols):
                # Skip if cell is not reachable yet or is a wall
                if distances[row][col] == float('inf') or grid[row][col] == 1:
                    continue
                
                # Check all neighbors (4-directional)
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    # Check if valid and walkable
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == 0):
                        
                        edge_weight = 1  # Uniform weight for grid
                        new_dist = distances[row][col] + edge_weight
                        
                        # Relax edge if distance can be improved
                        if new_dist < distances[new_row][new_col]:
                            distances[new_row][new_col] = new_dist
                            came_from[(new_row, new_col)] = (row, col)
                            updated = True
        
        # Early termination: if no updates, distances are finalized
        if not updated:
            break
    
    # Reconstruct path if reachable
    if distances[end[0]][end[1]] == float('inf'):
        return None
    
    path = []
    current = end
    
    # Reconstruct path from end to start
    while current != start:
        path.append(current)
        if current not in came_from:
            return None  # Path broken
        current = came_from[current]
    
    path.append(start)
    return path[::-1]  # Reverse to get start -> end


# Example usage and test
if __name__ == "__main__":
    # Create a sample grid (0 = walkable, 1 = wall)
    test_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0)
    end_pos = (4, 4)
    
    path = bellman_ford(test_grid, start_pos, end_pos)
    
    if path:
        print(f"Path found! Length: {len(path)}")
        print(f"Path: {path}")
    else:
        print("No path found")


