class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be isomorphic
        if len(s) != len(t):
            return False
            
        map_s_to_t = {}
        map_t_to_s = {}
        
        # Traverse both strings simultaneously
        for char_s, char_t in zip(s, t):
            # Check for conflicting mappings from s to t
            if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
                return False
                
            # Check for conflicting mappings from t to s
            if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
                return False
                
            # Establish the unique two-way mapping
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s
            
        return True