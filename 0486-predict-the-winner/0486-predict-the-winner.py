from functools import cache

class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        
        @cache
        def get_max_diff(left: int, right: int) -> int:
            # Base Case: Only one number remains
            if left == right:
                return nums[left]
                
            # Option A: Take the left element
            # The opponent gets the remaining range, so we subtract their optimal score
            take_left = nums[left] - get_max_diff(left + 1, right)
            
            # Option B: Take the right element
            take_right = nums[right] - get_max_diff(left, right - 1)
            
            # Return the path that gives us the best relative score
            return max(take_left, take_right)
            
        # If Player 1 can secure a net difference >= 0, they win or tie (which counts as a win)
        return get_max_diff(0, len(nums) - 1) >= 0
