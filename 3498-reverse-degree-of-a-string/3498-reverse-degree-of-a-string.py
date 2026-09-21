class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        
        for i, char in enumerate(s):
            # 1-indexed position of the character in the string
            string_pos = i + 1
            
            # Position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1)
            # ord('z') is 122, ord('a') is 97.
            alphabet_pos = 122 - ord(char) + 1
            
            total_sum += string_pos * alphabet_pos
            
        return total_sum
