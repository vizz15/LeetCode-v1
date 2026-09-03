class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_num=[x for x in nums1 if x % 2==1]

        if not odd_num:
            return True
        
        min_value=min(odd_num)

        for num  in nums1:
            if num % 2==0 and num < min_value:
                return False

        return True