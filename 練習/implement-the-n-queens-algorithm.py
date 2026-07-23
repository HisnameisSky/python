def dfs_n_queens(n: int) -> list:
    if n < 1:
        return []
        
    solutions = []
    
    def is_safe(board, row, col):
        for i in range(row):
            
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def dfs(row, current_board):
        if row == n:
            solutions.append(list(current_board))
            return
            
        for col in range(n):
            if is_safe(current_board, row, col):
                current_board.append(col)
                dfs(row + 1, current_board)
                current_board.pop()

    dfs(0, [])
    
    
    return solutions


if __name__ == '__main__':
    
    print("dfs_n_queens(1) ->", dfs_n_queens(1))
    
    
    print("dfs_n_queens(2) ->", dfs_n_queens(2))
    
    
    print("dfs_n_queens(4) ->", dfs_n_queens(4))
    
    print("len(dfs_n_queens(5)) ->", len(dfs_n_queens(5))) # 期待値: 10
    print("len(dfs_n_queens(8)) ->", len(dfs_n_queens(8))) # 期待値: 92