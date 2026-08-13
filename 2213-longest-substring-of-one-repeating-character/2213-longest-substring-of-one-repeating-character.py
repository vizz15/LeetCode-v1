class Node:
    def __init__(self, val=None):
        self.max_len = 1
        self.pref_len = 1
        self.suff_len = 1
        self.size = 1
        if val is not None:
            self.left_char = val
            self.right_char = val

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self.s = list(s)
        self.build(0, 0, self.n - 1)

    def merge(self, left: Node, right: Node) -> Node:
        parent = Node()
        parent.size = left.size + right.size
        parent.left_char = left.left_char
        parent.right_char = right.right_char
        
        # Base merge without bridging across the boundary
        parent.max_len = max(left.max_len, right.max_len)
        parent.pref_len = left.pref_len
        parent.suff_len = right.suff_len

        # If adjacent characters match, combine suffix and prefix
        if left.right_char == right.left_char:
            combined = left.suff_len + right.pref_len
            parent.max_len = max(parent.max_len, combined)
            
            if left.pref_len == left.size:
                parent.pref_len = left.size + right.pref_len
            if right.suff_len == right.size:
                parent.suff_len = right.size + left.suff_len
                
        return parent

    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = Node(self.s[start])
            return
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, start: int, end: int, idx: int, ch: str):
        if start == end:
            self.s[idx] = ch
            self.tree[node] = Node(ch)
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, ch)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, ch)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(s)
        ans = []
        
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(0, 0, st.n - 1, idx, ch)
            ans.append(st.tree[0].max_len)
            
        return ans

        