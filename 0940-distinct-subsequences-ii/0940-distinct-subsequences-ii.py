class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Maps each character ('a' through 'z') to the number of subsequences 
        # it uniquely generated during its most recent occurrence.
        last_added_by_char = {}
        
        # Tracks total distinct subsequences formed so far
        total_subsequences = 0 
        
        for char in s:
            # 1. Calculate how many new subsequences this character can build.
            # It can be appended to all existing subsequences (+1 for the single character itself)
            new_additions = (total_subsequences + 1) % MOD
            
            # 2. Calculate the next total before adjusting for duplicates
            next_total = (total_subsequences + new_additions) % MOD
            
            # 3. Deduct duplicates if we have seen this character before
            if char in last_added_by_char:
                next_total = (next_total - last_added_by_char[char]) % MOD
                
            # Update our character history ledger and running total
            last_added_by_char[char] = new_additions
            total_subsequences = next_total
            
        # Modulo arithmetic in Python can yield negative numbers during subtraction,
        # so adding MOD ensures it stays non-negative before returning.
        return (total_subsequences + MOD) % MOD
