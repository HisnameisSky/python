def hanoi_solver(n):
    
    rods = [list(range(n, 0, -1)), [], []]
    
    history = []
    
    def record_state():
        
        state_str = f"{rods[0]} {rods[1]} {rods[2]}"
        history.append(state_str)

    record_state()

    
    def move_disks(count, source, target, auxiliary):
        if count > 0:
            move_disks(count - 1, source, auxiliary, target)
            
            disk = rods[source].pop()
            rods[target].append(disk)
            
            record_state()
            
            move_disks(count - 1, auxiliary, target, source)

    move_disks(n, 0, 2, 1)
    
    return "\n".join(history)


if __name__ == '__main__':
    print("--- hanoi_solver(2) ---")
    print(hanoi_solver(2))
    
    print("\n--- hanoi_solver(3) ---")
    print(hanoi_solver(3))