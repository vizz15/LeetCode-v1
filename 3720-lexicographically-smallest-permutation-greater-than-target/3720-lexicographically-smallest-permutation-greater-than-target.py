from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        # 1. Count the available characters in s
        counts = Counter(s)
        
        # Track the characters we tentatively match with target
        matched_prefix = []
        
        # 2. Try to greedily match the target prefix from left to right
        for char in target:
            if counts[char] > 0:
                counts[char] -= 1
                matched_prefix.append(char)
            else:
                break
                
        # 3. Backtrack from the rightmost position to find the pivot
        # We search from the end of our matched prefix down to index 0
        for i in range(len(matched_prefix), -1, -1):
            # If we are backtracking from an already matched character, 
            # put it back into the frequency bank
            if i < len(matched_prefix):
                counts[matched_prefix[i]] += 1
            
            # The target character at this position
            if i < n:
                target_char = target[i]
                
                # Look for the smallest available character strictly greater than target_char
                for ascii_val in range(ord(target_char) + 1, ord('z') + 1):
                    next_char = chr(ascii_val)
                    
                    if counts[next_char] > 0:
                        # Pivot found! Claim this character
                        counts[next_char] -= 1
                        
                        # Construct the final string:
                        # Prefix (up to i) + Next greater char + Sorted remaining characters
                        prefix = target[:i] + next_char
                        suffix = "".join(sorted(counts.elements()))
                        
                        return prefix + suffix
                        
        # If no valid pivot can make the permutation strictly greater
        return ""
