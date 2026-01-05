from collections import deque

def bidirectional_search(grid, start, end):
    """
    Bidirectional Search Pathfinding Algorithm
    Time Complexity: O(b^(d/2)) where b is branching factor and d is depth
    Space Complexity: O(b^(d/2))
    
    Bidirectional search runs two simultaneous BFS searches - one from start and one from end.
    When the searches meet, we've found the shortest path. Significantly reduces search space.
    Works best for unweighted graphs where shortest path is guaranteed.
    
    Args:
        grid (list): 2D grid representing the map (0 = walkable, 1 = wall)
        start (tuple): Starting position (row, col)
        end (tuple): Target position (row, col)
        
    Returns:
        list: Path from start to end as list of (row, col) tuples, or None if no path exists
    """
    rows, cols = len(grid), len(grid[0])
    
    # Check if start and end are the same
    if start == end:
        return [start]
    
    # Forward search (from start)
    forward_queue = deque([start])
    forward_visited = {start}
    forward_parent = {start: None}
    
    # Backward search (from end)
    backward_queue = deque([end])
    backward_visited = {end}
    backward_parent = {end: None}
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    meeting_point = None
    iteration = 0
    
    while forward_queue and backward_queue and not meeting_point:
        iteration += 1
        
        # Alternate between forward and backward search
        if iteration % 2 == 1:
            # Forward search turn
            current_queue = forward_queue
            current_visited = forward_visited
            current_parent = forward_parent
            opposite_visited = backward_visited
            search_direction = "forward"
        else:
            # Backward search turn
            current_queue = backward_queue
            current_visited = backward_visited
            current_parent = backward_parent
            opposite_visited = forward_visited
            search_direction = "backward"
        
        if not current_queue:
            continue
            
        current = current_queue.popleft()
        
        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = current[0] + dr, current[1] + dc
            
            # Check bounds
            if (new_row < 0 or new_row >= rows or 
                new_col < 0 or new_col >= cols):
                continue
                
            # Check if cell is walkable
            if grid[new_row][new_col] == 1:  # 1 represents wall
                continue
                
            new_pos = (new_row, new_col)
            
            # Check if already visited by current search
            if new_pos in current_visited:
                continue
            
            # Check if this node is visited by the opposite search (meeting point)
            if new_pos in opposite_visited:
                meeting_point = new_pos
                current_parent[new_pos] = current
                break
            
            # Add to current search
            current_visited.add(new_pos)
            current_parent[new_pos] = current
            current_queue.append(new_pos)
    
    if meeting_point:
        # Reconstruct path from start to meeting point
        forward_path = []
        current = meeting_point
        while current is not None:
            forward_path.append(current)
            current = forward_parent[current]
        forward_path.reverse()  # Reverse to get start to meeting point
        
        # Reconstruct path from end to meeting point
        backward_path = []
        current = meeting_point
        while current is not None:
            backward_path.append(current)
            current = backward_parent[current]
        backward_path = backward_path[1:]  # Remove meeting point (duplicate) - O(1) instead of O(n)
        
        # Combine paths
        full_path = forward_path + backward_path
        return full_path
    
    return None  # No path found


# Example usage and testing
if __name__ == "__main__":
    # Example grid (0 = walkable, 1 = wall)
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    start = (0, 0)
    end = (4, 4)
    
    path = bidirectional_search(grid, start, end)
    
    if path:
        print(f"Path found: {path}")
        print(f"Path length: {len(path)}")
    else:
        print("No path found")


