from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Step 1: Map each row to a set of its reserved seats
        occupied = defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:  # We only care about seats 2 through 9
                occupied[row].add(seat)
        
        # Step 2: Start by assuming ALL rows are completely empty (2 groups per row)
        max_groups = n * 2
        
        # Step 3: Deduct groups for the rows that actually have reservations
        for row, seats in occupied.items():
            left_free = not (2 in seats or 3 in seats or 4 in seats or 5 in seats)
            right_free = not (6 in seats or 7 in seats or 8 in seats or 9 in seats)
            mid_free = not (4 in seats or 5 in seats or 6 in seats or 7 in seats)
            
            # Reduce the initially assumed 2 groups based on actual availability
            if left_free and right_free:
                continue  # Keeps 2 groups (no reduction)
            elif left_free or right_free or mid_free:
                max_groups -= 1  # Can only fit 1 group instead of 2
            else:
                max_groups -= 2  # Cannot fit any group instead of 2
                
        return max_groups
