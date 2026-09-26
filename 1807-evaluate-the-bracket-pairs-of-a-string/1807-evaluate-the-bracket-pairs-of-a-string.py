class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Convert the knowledge list into a hash map for O(1) lookups
        k_map = {key: value for key, value in knowledge}
        
        result = []
        is_inside_bracket = False
        current_key = []
        
        # Step 2: Parse the string sequentially
        for char in s:
            if char == '(':
                is_inside_bracket = True
            elif char == ')':
                is_inside_bracket = False
                key_str = "".join(current_key)
                
                # Look up the key in our map, defaulting to "?" if not found
                result.append(k_map.get(key_str, "?"))
                current_key = []  # Reset for the next bracket pair
            else:
                if is_inside_bracket:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)
