class SegmentNode:
    def __init__(self, k: int):
        self.prod = 1
        self.remain = [0] * k

class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [SegmentNode(k) for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)
        
    def merge(self, left: SegmentNode, right: SegmentNode) -> SegmentNode:
        parent = SegmentNode(self.k)
        # Combined range product is simply the product of left and right segments
        parent.prod = (left.prod * right.prod) % self.k
        
        # Prefixes originating from the left boundary:
        # 1. Any valid prefix entirely within the left child
        for r in range(self.k):
            parent.remain[r] += left.remain[r]
            
        # 2. Any prefix that spans across the left child and extends into the right child
        # The product will be (left.prod * right_prefix_rem) % k
        for r in range(self.k):
            if right.remain[r] > 0:
                new_rem = (left.prod * r) % self.k
                parent.remain[new_rem] += right.remain[r]
                
        return parent

    def build(self, nums: list[int], node: int, start: int, end: int):
        if start == end:
            val_mod = nums[start] % self.k
            self.tree[node].prod = val_mod
            self.tree[node].remain[val_mod] = 1
            return
        
        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            val_mod = val % self.k
            self.tree[node].prod = val_mod
            self.tree[node].remain = [0] * self.k
            self.tree[node].remain[val_mod] = 1
            return
            
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node: int, start: int, end: int, l: int, r: int) -> SegmentNode:
        if l <= start and end <= r:
            return self.tree[node]
            
        mid = (start + end) // 2
        if r <= mid:
            return self.query(2 * node + 1, start, mid, l, r)
        if l > mid:
            return self.query(2 * node + 2, mid + 1, end, l, r)
            
        left_res = self.query(2 * node + 1, start, mid, l, mid)
        right_res = self.query(2 * node + 2, mid + 1, end, mid + 1, r)
        return self.merge(left_res, right_res)

class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        result = []
        
        for index, value, start, x in queries:
            # Step 1: Persistently update the value at index
            tree.update(0, 0, n - 1, index, value)
            
            # Step 2: Query the active range from 'start' to the end of the array
            node_res = tree.query(0, 0, n - 1, start, n - 1)
            
            # Extract the count of prefix matches for target remainder x
            result.append(node_res.remain[x])
            
        return result
