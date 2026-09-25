class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # The stack will hold elements representing current evaluation contexts
        # Elements can be: '{', ',', or a set of strings
        stack = []
        
        i = 0
        n = len(expression)
        
        while i < n:
            char = expression[i]
            
            if char == '{':
                stack.append('{')
                i += 1
                
            elif char == ',':
                stack.append(',')
                i += 1
                
            elif char == '}':
                # Process everything inside the current matching braces
                # Step 1: Collect sets separated by commas to perform Union
                group = []
                while stack and stack[-1] != '{':
                    top = stack.pop()
                    if top != ',':
                        group.append(top)
                
                # Pop the opening brace '{'
                if stack and stack[-1] == '{':
                    stack.pop()
                
                # Perform the union of all sets in the current level
                # For example: [{"c"}, {"a", "b"}] -> {"a", "b", "c"}
                combined_set = set()
                for s in group:
                    combined_set.update(s)
                
                # Step 2: Handle implicit concatenation with whatever is immediately left of '{'
                # E.g., if we had "a" followed by the result of "{b,c}", we multiply them
                if stack and isinstance(stack[-1], set):
                    left_set = stack.pop()
                    new_set = {l + r for l in left_set for r in combined_set}
                    stack.append(new_set)
                else:
                    stack.append(combined_set)
                i += 1
                
            else:
                # Read a contiguous sequence of lowercase letters
                start = i
                while i < n and expression[i].isalpha():
                    i += 1
                word = expression[start:i]
                current_set = {word}
                
                # If there's already a set right before it, implicitly concatenate them
                # E.g., "{a,b}c" -> {"ac", "bc"}
                if stack and isinstance(stack[-1], set):
                    left_set = stack.pop()
                    current_set = {l + r for l in left_set for r in current_set}
                
                stack.append(current_set)
        
        # At the end of parsing, the stack will contain sets and commas representing the root level
        # Collapse remaining root level elements via Union
        final_set = set()
        for item in stack:
            if isinstance(item, set):
                final_set.update(item)
                
        # Return the final result sorted alphabetically
        return sorted(list(final_set))
