class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        
        # Track the first and last occurrence of each character
        leftmost = {}
        rightmost = {}
        for i, char in enumerate(s):
            if char not in leftmost:
                leftmost[char] = i
            rightmost[char] = i
            
        def get_new_right(i: int) -> int:
            right = rightmost[s[i]]
            j = i
            while j <= right:
                # If a character within the span starts before index i,
                # then index i cannot be a valid starting boundary.
                if leftmost[s[j]] < i:
                    return -1
                right = max(right, rightmost[s[j]])
                j += 1
            return right

        ans = []
        last_right = -1
        
        for i in range(n):
            # Only process if this is the first time we see the character
            if i == leftmost[s[i]]:
                r = get_new_right(i)
                if r != -1:
                    # If the new valid substring is completely wrapped inside 
                    # the previous one, we drop the larger one to maximize counts
                    if r <= last_right:
                        ans.pop()
                    ans.append(s[i : r + 1])
                    last_right = r
                    
        return ans
