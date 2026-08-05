from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Step 1: Build an adjacency list representation of the graph
        graph = {i: [] for i in range(n)}
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 2: Run BFS/DFS to identify all suspicious methods starting from k
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # If an external method triggers a suspicious one, nothing can be removed
                return list(range(n))
                
        # Step 4: Safely return only the remaining non-suspicious methods
        return [i for i in range(n) if i not in suspicious]
