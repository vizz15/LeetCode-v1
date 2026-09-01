from collections import deque

class Solution:
    def minMoves(self, classroom: list[list[str]], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        max_energy = energy
        
        start_r, start_col = 0, 0
        litter_map = {}
        litter_idx = 0
        
        # 1. Scan the grid to find the start position and catalog all litter
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_col = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_idx
                    litter_idx += 1
                    
        num_litter = len(litter_map)
        target_mask = (1 << num_litter) - 1
        
        # If there is no litter to collect, we are already done
        if num_litter == 0:
            return 0
            
        # 2. Initialize BFS Queue and Visited state set
        # Queue state structure: (row, col, current_energy, litter_mask)
        q = deque([(start_r, start_col, max_energy, 0)])
        visited = {(start_r, start_col, max_energy, 0)}
        
        moves = 0
        
        # 3. Standard level-by-level BFS traversal
        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()
                
                # If all litter pieces are collected, return the move count
                if mask == target_mask:
                    return moves
                
                # If energy reaches 0 and we aren't refreshed, we cannot make any further moves
                if e == 0:
                    continue
                    
                # Explore all four adjacent neighbors
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    # Ensure neighbor is inside boundaries and not an obstacle
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                        ne = e - 1
                        nmask = mask
                        
                        # Apply energy replenishment rule
                        if classroom[nr][nc] == 'R':
                            ne = max_energy
                            
                        # Apply litter pickup collection rule
                        if classroom[nr][nc] == 'L' and (nr, nc) in litter_map:
                            nmask |= (1 << litter_map[(nr, nc)])
                            
                        next_state = (nr, nc, ne, nmask)
                        if next_state not in visited:
                            visited.add(next_state)
                            q.append(next_state)
                            
            moves += 1
            
        return -1

        