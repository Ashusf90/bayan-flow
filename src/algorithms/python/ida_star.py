def ida_star(grid, start, end, rows, cols):
    def manhattan_distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def search(path, g, threshold):
        current = path[-1]
        f = g + manhattan_distance(current, end)

        if f > threshold:
            return False, f
            
        if current == end:
            return True, f

        min_threshold = float('inf')
        
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            next_node = (current[0] + dr, current[1] + dc)
            
            if (0 <= next_node[0] < rows and 
                0 <= next_node[1] < cols and 
                next_node not in path):
                
                path.append(next_node)
                found, next_threshold = search(path, g + 1, threshold)
                
                if found:
                    return True, next_threshold
                    
                if next_threshold < min_threshold:
                    min_threshold = next_threshold
                    
                path.pop()

        return False, min_threshold

    threshold = manhattan_distance(start, end)
    path = [start]

    while True:
        found, next_threshold = search(path, 0, threshold)
        if found:
            return path
        if next_threshold == float('inf'):
            return None
        threshold = next_threshold


