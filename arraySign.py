class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def arraySign(self, nums: List[int]) -> int:
        '''
        Start with prod = 1. 
        If there is a 0 in the array the answer is 0
        To avoid overflow make all the negative numbers -1 and 
        all positive numbers 1 and calculate the prod
        '''
        prod = 1
        for num in nums:
            if num < 0:
                prod = prod * -1
            elif num == 0:
                return 0
        return prod


        
