def adjacency_list_to_matrix(adj_list):
    num_nodes = len(adj_list)
    
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
            
    for row in matrix:
        print(row)
        
    return matrix


if __name__ == '__main__':
    
    print("--- テスト7の実行結果 ---")
    list1 = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}
    result1 = adjacency_list_to_matrix(list1)
    print("返り値:", result1)
    
    print("\n--- テスト9の実行結果 ---")
    list2 = {0: [], 1: [], 2: []}
    result2 = adjacency_list_to_matrix(list2)
    print("返り値:", result2)