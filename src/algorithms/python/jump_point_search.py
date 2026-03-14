import heapq
import math

def heuristic(a, b):
    """
    Calculate Manhattan distance heuristic between two points.
    
    Args:
        a (tuple): First point (row, col)
        b (tuple): Second point (row, col)
        
    Returns:
        int: Manhattan distance
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_valid(row, col, rows, cols):
    """Check if position is within grid bounds."""
    return 0 <= row < rows and 0 <= col < cols


def is_walkable(row, col, grid):
    """Check if cell is walkable (0 = walkable, 1 = wall)."""
    return grid[row][col] == 0


def identify_forced_neighbors(row, col, dx, dy, rows, cols, grid):
    """
    Identify forced neighbors for Jump Point Search.
    Forced neighbors are nodes that must be considered when moving
    in a direction because obstacles block the natural path.
    
    Args:
        row (int): Current row
        col (int): Current column
        dx (int): X direction (-1, 0, or 1)
        dy (int): Y direction (-1, 0, or 1)
        rows (int): Total rows
        cols (int): Total columns
        grid (list): Grid with cell weights
        
    Returns:
        list: List of forced neighbor positions (row, col)
    """
    forced_neighbors = []
    
    # Cardinal directions (dx or dy is 0)
    if dx == 0:
        # Moving vertically (up or down)
        left_blocked = not is_valid(row, col - 1, rows, cols) or \
                      not is_walkable(row, col - 1, grid)
        right_blocked = not is_valid(row, col + 1, rows, cols) or \
                       not is_walkable(row, col + 1, grid)
        
        if left_blocked and is_valid(row + dy, col - 1, rows, cols) and \
           is_walkable(row + dy, col - 1, grid):
            forced_neighbors.append((row + dy, col - 1))
        if right_blocked and is_valid(row + dy, col + 1, rows, cols) and \
           is_walkable(row + dy, col + 1, grid):
            forced_neighbors.append((row + dy, col + 1))
    elif dy == 0:
        # Moving horizontally (left or right)
        up_blocked = not is_valid(row - 1, col, rows, cols) or \
                    not is_walkable(row - 1, col, grid)
        down_blocked = not is_valid(row + 1, col, rows, cols) or \
                      not is_walkable(row + 1, col, grid)
        
        if up_blocked and is_valid(row - 1, col + dx, rows, cols) and \
           is_walkable(row - 1, col + dx, grid):
            forced_neighbors.append((row - 1, col + dx))
        if down_blocked and is_valid(row + 1, col + dx, rows, cols) and \
           is_walkable(row + 1, col + dx, grid):
            forced_neighbors.append((row + 1, col + dx))
    else:
        # Diagonal movement
        natural_row = row + dy
        natural_col = col
        natural_row2 = row
        natural_col2 = col + dx
        
        natural1_blocked = not is_valid(natural_row, natural_col, rows, cols) or \
                          not is_walkable(natural_row, natural_col, grid)
        natural2_blocked = not is_valid(natural_row2, natural_col2, rows, cols) or \
                          not is_walkable(natural_row2, natural_col2, grid)
        
        # Forced neighbors for diagonal
        if natural1_blocked and is_valid(natural_row, col + dx, rows, cols) and \
           is_walkable(natural_row, col + dx, grid):
            forced_neighbors.append((natural_row, col + dx))
        if natural2_blocked and is_valid(row + dy, natural_col2, rows, cols) and \
           is_walkable(row + dy, natural_col2, grid):
            forced_neighbors.append((row + dy, natural_col2))
    
    return forced_neighbors


def jump(row, col, dx, dy, end, rows, cols, grid, closed):
    """
    Jump in a direction until finding a jump point or hitting an obstacle.
    
    Args:
        row (int): Starting row
        col (int): Starting column
        dx (int): X direction (-1, 0, or 1)
        dy (int): Y direction (-1, 0, or 1)
        end (tuple): End position (row, col)
        rows (int): Total rows
        cols (int): Total columns
        grid (list): Grid with cell weights
        closed (set): Closed set (visited nodes)
        
    Returns:
        tuple|None: Jump point position (row, col) or None
    """
    current_row, current_col = row, col
    
    while True:
        current_row += dy
        current_col += dx
        
        # Check bounds
        if not is_valid(current_row, current_col, rows, cols):
            return None
        
        # Check if walkable
        if not is_walkable(current_row, current_col, grid):
            return None
        
        # Check if goal
        if (current_row, current_col) == end:
            return (current_row, current_col)
        
        # Check for forced neighbors
        forced_neighbors = identify_forced_neighbors(
            current_row, current_col, dx, dy, rows, cols, grid
        )
        
        if forced_neighbors:
            return (current_row, current_col)
        
        # If diagonal, check for jump points in natural directions
        if dx != 0 and dy != 0:
            # Try jumping in X direction
            jump_x = jump(
                current_row, current_col - dx, dx, 0,
                end, rows, cols, grid, closed
            )
            if jump_x:
                return (current_row, current_col)
            
            # Try jumping in Y direction
            jump_y = jump(
                current_row - dy, current_col, 0, dy,
                end, rows, cols, grid, closed
            )
            if jump_y:
                return (current_row, current_col)


def jump_point_search(grid, start, end):
    """
    Jump Point Search (JPS) Pathfinding Algorithm
    Time Complexity: O(E) where E is number of edges
    Space Complexity: O(V) where V is number of vertices
    
    JPS optimizes A* by eliminating symmetric paths on uniform-cost grids.
    It only explores "jump points" - nodes that could improve the path.
    
    Args:
        grid (list): 2D grid representing the map (0 = walkable, 1 = wall)
        start (tuple): Starting position (row, col)
        end (tuple): Target position (row, col)
        
    Returns:
        list: Path from start to end as list of (row, col) tuples, or None if no path exists
    """
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue: stores (f_score, g_score, row, col)
    pq = [(heuristic(start, end), 0, start[0], start[1])]
    
    # Dictionary to store g_score (cost from start) for each cell
    g_scores = {start: 0}
    
    # Dictionary to reconstruct the path
    came_from = {}
    
    # Set to track closed (visited) nodes
    closed = set()
    
    # 8-directional movement (cardinal + diagonal)
    directions = [
        (-1, 0),   # up
        (1, 0),    # down
        (0, -1),   # left
        (0, 1),    # right
        (-1, -1),  # up-left
        (-1, 1),   # up-right
        (1, -1),   # down-left
        (1, 1),    # down-right
    ]
    
    while pq:
        current_f, current_g, row, col = heapq.heappop(pq)
        current = (row, col)
        
        # Skip if already processed with better cost
        if current in closed:
            continue
        
        closed.add(current)
        
        # If we reached the end, reconstruct the path
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to get start -> end
        
        # Get parent direction (if exists)
        parent_dir = None
        if current in came_from:
            parent = came_from[current]
            parent_dir = (current[0] - parent[0], current[1] - parent[1])
        
        # Explore neighbors (pruning: only check parent direction if exists)
        neighbors_to_check = [parent_dir] if parent_dir else directions
        
        for dy, dx in neighbors_to_check:
            jump_point = jump(
                row, col, dx, dy, end, rows, cols, grid, closed
            )
            
            if not jump_point:
                continue
            
            new_row, new_col = jump_point
            
            if (new_row, new_col) in closed:
                continue
            
            # Calculate cost (diagonal vs cardinal)
            is_diagonal = dx != 0 and dy != 0
            move_cost = math.sqrt(2) if is_diagonal else 1
            tentative_g = current_g + move_cost
            
            if tentative_g < g_scores.get((new_row, new_col), float('inf')):
                came_from[(new_row, new_col)] = current
                g_scores[(new_row, new_col)] = tentative_g
                
                # Calculate f_score = g + h
                h_score = heuristic((new_row, new_col), end)
                f_score = tentative_g + h_score
                
                heapq.heappush(pq, (f_score, tentative_g, new_row, new_col))
    
    # No path found
    return None


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
    
    print(f"Grid size: {len(test_grid)}x{len(test_grid[0])}")
    print(f"Start: {start_pos}, End: {end_pos}")
    print(f"Heuristic (Manhattan distance): {heuristic(start_pos, end_pos)}")
    
    path = jump_point_search(test_grid, start_pos, end_pos)
    
    if path:
        print(f"\nPath found with {len(path)} steps:")
        print(f"Path: {path}")
        print(f"Actual distance: {len(path) - 1}")
    else:
        print("No path found!")
    
    # Visualize the path on the grid
    if path:
        print("\nGrid with path (. = walkable, # = wall, * = path):")
        for i in range(len(test_grid)):
            row_str = ""
            for j in range(len(test_grid[0])):
                if (i, j) in path:
                    row_str += "* "
                elif test_grid[i][j] == 1:
                    row_str += "# "
                else:
                    row_str += ". "
            print(row_str)

