from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # last[j] stores the largest index in word1 from which
        # the suffix word2[j:] can be completely matched.
        last = [-1] * (m + 1)
        last[m] = n

        # Fill the 'last' array from right to left
        w2_idx = m - 1
        for w1_idx in range(n - 1, -1, -1):
            if w2_idx >= 0 and word1[w1_idx] == word2[w2_idx]:
                last[w2_idx] = w1_idx
                w2_idx -= 1

        result = []
        w1_idx = 0
        w2_idx = 0
        changed = False  # Tracks if we have used our single allowed mutation

        while w2_idx < m and w1_idx < n:
            if word1[w1_idx] == word2[w2_idx]:
                # Exact match: greedily accept this index to keep it as small as possible
                result.append(w1_idx)
                w2_idx += 1
            else:
                # Mismatch: Check if we can change this character
                # We can change it if we haven't used our mutation yet AND the remaining 
                # suffix of word2 can be fully matched by the remaining part of word1.
                if not changed and last[w2_idx + 1] > w1_idx:
                    result.append(w1_idx)
                    w2_idx += 1
                    changed = True  # Consume our one-time modification allowance
            w1_idx += 1

        # If we successfully matched the entirety of word2, return the sequence, else []
        return result if len(result) == m else []

        
        