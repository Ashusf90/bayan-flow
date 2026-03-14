import heapq
from typing import List, Tuple, Optional, Dict, Set


def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """
    Calculate Manhattan distance heuristic between two points.
    
    Args:
        a (tuple): First point (row, col)
        b (tuple): Second point (row, col)
        
    Returns:
        int: Manhattan distance
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def calculate_key(
    node: Tuple[int, int],
    start: Tuple[int, int],
    g_values: Dict[Tuple[int, int], float],
    rhs_values: Dict[Tuple[int, int], float],
    km: int,
) -> Tuple[float, float]:
    """
    Calculate D* Lite priority key for a node.
    
    Key formula: k(n) = [min(g(n), rhs(n)) + h(n) + km, min(g(n), rhs(n))]
    
    Args:
        node (tuple): Node position (row, col)
        start (tuple): Start position for heuristic calculation
        g_values (dict): g-value mapping (cost from node to start)
        rhs_values (dict): rhs-value mapping (lookahead cost)
        km (int): Key modifier (for incremental updates)
        
    Returns:
        tuple: Key as (k1, k2) for priority queue ordering
    """
    min_val = min(g_values.get(node, float('inf')), rhs_values.get(node, float('inf')))
    k1 = min_val + heuristic(start, node) + km
    k2 = min_val
    return (k1, k2)


def d_star_lite(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    D* Lite Pathfinding Algorithm
    
    Time Complexity: O((V + E) log V) for initial search
    Space Complexity: O(V)
    
    D* Lite is an incremental heuristic search algorithm optimized for dynamic environments.
    Unlike A*, it can efficiently handle graph changes and re-plan paths when obstacles appear.
    
    Key Features:
    - Searches backward from goal to start
    - Maintains g-values (costs) and rhs-values (lookahead costs)
    - Detects consistency violations and updates only affected nodes
    - Uses priority queue with two-part keys for ordering
    - Supports incremental replanning (not shown in this static version)
    
    Algorithm Steps:
    1. Initialize: Set rhs(goal) = 0, all other rhs = ∞, all g = ∞
    2. Insert goal in priority queue with calculated key
    3. While priority queue not empty:
       a. Pop node u with minimum key
       b. If u is over-consistent (g > rhs): Update g, add neighbors to queue
       c. If u is under-consistent (g < rhs): Set g = ∞, re-evaluate and add to queue
    4. Reconstruct path from start to goal using g-values
    
    Args:
        grid (list): 2D grid (0 = walkable, 1 = wall/obstacle)
        start (tuple): Starting position (row, col)
        end (tuple): Goal position (row, col)
        
    Returns:
        list: Path from start to end as list of tuples, or None if no path exists
        
    Raises:
        ValueError: If grid is empty or positions are out of bounds
    """
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    rows, cols = len(grid), len(grid[0])
    
    # Validate start and end positions
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        raise ValueError(f"Start position {start} out of bounds")
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        raise ValueError(f"End position {end} out of bounds")
    
    # Handle start == end case
    if start == end:
        return [start]
    
    # Initialize g-values and rhs-values for all nodes
    g_values: Dict[Tuple[int, int], float] = {}
    rhs_values: Dict[Tuple[int, int], float] = {}
    
    # Priority queue: (key, counter, node) for stable sorting
    # Using counter to break ties and ensure FIFO order for equal keys
    pq: List[Tuple[Tuple[float, float], int, Tuple[int, int]]] = []
    counter = 0
    
    # Set of nodes in priority queue (for lazy deletion)
    in_queue: Set[Tuple[int, int]] = set()
    
    # Initialize: rhs(goal) = 0, all others = ∞
    rhs_values[end] = 0
    key = calculate_key(end, start, g_values, rhs_values, 0)
    heapq.heappush(pq, (key, counter, end))
    in_queue.add(end)
    counter += 1
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # ComputeShortestPath: main D* Lite loop
    while pq:
        # Pop minimum key node
        (k_old, _, u) = heapq.heappop(pq)
        in_queue.discard(u)
        
        # Lazy deletion: verify key is current
        k_new = calculate_key(u, start, g_values, rhs_values, 0)
        if k_old > k_new:
            # Outdated entry, re-insert with new key
            heapq.heappush(pq, (k_new, counter, u))
            in_queue.add(u)
            counter += 1
            continue
        
        # Check termination condition: key >= start's key AND start is consistent
        start_key = calculate_key(start, start, g_values, rhs_values, 0)
        if k_new >= start_key and rhs_values.get(start, float('inf')) == g_values.get(start, float('inf')):
            # Shortest path found
            break
        
        g_u = g_values.get(u, float('inf'))
        rhs_u = rhs_values.get(u, float('inf'))
        
        if g_u > rhs_u:
            # Over-consistent: update g-value
            g_values[u] = rhs_u
            
            # Update predecessors (nodes that could reach u)
            for dr, dc in directions:
                s = (u[0] + dr, u[1] + dc)
                
                # Check bounds
                if not (0 <= s[0] < rows and 0 <= s[1] < cols):
                    continue
                
                # Skip if wall
                if grid[s[0]][s[1]] == 1:
                    continue
                
                # Skip goal node
                if s == end:
                    continue
                
                # Update rhs(s) = min(rhs(s), g(u) + 1)
                old_rhs = rhs_values.get(s, float('inf'))
                new_rhs = min(old_rhs, g_values.get(u, float('inf')) + 1)
                rhs_values[s] = new_rhs
                
                # If s inconsistent, add to queue
                if g_values.get(s, float('inf')) != rhs_values[s]:
                    key_s = calculate_key(s, start, g_values, rhs_values, 0)
                    heapq.heappush(pq, (key_s, counter, s))
                    in_queue.add(s)
                    counter += 1
        else:
            # Under-consistent: set g to infinity and re-evaluate
            g_values[u] = float('inf')
            
            # Re-evaluate u itself
            if u != end:
                old_rhs = rhs_values.get(u, float('inf'))
                # Find minimum rhs based on neighbors
                min_rhs = float('inf')
                for dr, dc in directions:
                    s = (u[0] + dr, u[1] + dc)
                    if 0 <= s[0] < rows and 0 <= s[1] < cols and grid[s[0]][s[1]] == 0:
                        min_rhs = min(min_rhs, g_values.get(s, float('inf')) + 1)
                rhs_values[u] = min_rhs
            
            # Update u if needed
            if g_values.get(u, float('inf')) != rhs_values.get(u, float('inf')):
                key_u = calculate_key(u, start, g_values, rhs_values, 0)
                heapq.heappush(pq, (key_u, counter, u))
                in_queue.add(u)
                counter += 1
            
            # Re-evaluate predecessors
            for dr, dc in directions:
                s = (u[0] + dr, u[1] + dc)
                
                # Check bounds
                if not (0 <= s[0] < rows and 0 <= s[1] < cols):
                    continue
                
                # Skip if wall
                if grid[s[0]][s[1]] == 1:
                    continue
                
                # Skip goal
                if s == end:
                    continue
                
                # Recalculate rhs(s)
                min_rhs = float('inf')
                for dr2, dc2 in directions:
                    s2 = (s[0] + dr2, s[1] + dc2)
                    if 0 <= s2[0] < rows and 0 <= s2[1] < cols and grid[s2[0]][s2[1]] == 0:
                        min_rhs = min(min_rhs, g_values.get(s2, float('inf')) + 1)
                rhs_values[s] = min_rhs
                
                # If inconsistent, add to queue
                if g_values.get(s, float('inf')) != rhs_values[s]:
                    key_s = calculate_key(s, start, g_values, rhs_values, 0)
                    heapq.heappush(pq, (key_s, counter, s))
                    in_queue.add(s)
                    counter += 1
    
    # No path found
    if g_values.get(start, float('inf')) == float('inf'):
        return None
    
    # Reconstruct path from start to end
    path = [start]
    current = start
    
    while current != end:
        # Find neighbor with minimum g-value
        min_g = float('inf')
        next_node = None
        
        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue
            
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
            
            g_neighbor = g_values.get(neighbor, float('inf'))
            if g_neighbor < min_g:
                min_g = g_neighbor
                next_node = neighbor
        
        if next_node is None or min_g == float('inf'):
            # No valid next node - shouldn't happen if algorithm is correct
            return None
        
        current = next_node
        path.append(current)
    
    return path
