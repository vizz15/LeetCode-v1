class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        opened = []
        # pair[i] will store the index of the matching bracket for s[i]
        pair = [0] * n
        
        # Step 1: Precompute the matching pairs using a stack
        for i, char in enumerate(s):
            if char == '(':
                opened.append(i)
            elif char == ')':
                j = opened.pop()
                pair[i] = j
                pair[j] = i
                
        # Step 2: Traverse the string, changing direction at brackets
        result = []
        curr_index = 0
        direction = 1  # 1 means moving forward, -1 means moving backward
        
        while curr_index < n:
            if s[curr_index] == '(' or s[curr_index] == ')':
                # Teleport to the matching bracket position
                curr_index = pair[curr_index]
                # Reverse the traversing direction
                direction = -direction
            else:
                # Append standard lowercase characters to result
                result.append(s[curr_index])
                
            curr_index += direction
            
        return "".join(result)
