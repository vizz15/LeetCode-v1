class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. Join all digits together into a single string: [1, 2, 3] -> "123"
        num_str = "".join(str(d) for d in digits)
        
        # 2. Convert to integer and add 1: "123" -> 123 -> 124
        new_num = int(num_str) + 1
        
        # 3. Convert back into a list of integers: 124 -> "124" -> [1, 2, 4]
        return [int(d) for d in str(new_num)]

            


        