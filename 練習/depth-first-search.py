def dfs(matrix, start_node):
    visited = []
    
    stack = [start_node]
    
    while stack:
        
        current = stack.pop()
        
        if current not in visited:
            
            visited.append(current)
            
            
            for neighbor in range(len(matrix[current])):
                if matrix[current][neighbor] == 1:
                    
                    stack.append(neighbor)
                    
    return visited


if __name__ == '__main__':
    
    print("Test 2:", dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
    
    print("Test 4:", dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
    
    
    print("Test 5:", dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3))
