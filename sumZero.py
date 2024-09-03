class Solution:
    """
    Time Complexity: O(n/2)= O(n)
    Space Complexity: O(n)
    """
    def sumZero(self, n: int) -> List[int]:
        res = []  # Initialize an empty list to store the result
        mid = n // 2  # Calculate the midpoint of n
        
        if n % 2 == 1:  # If n is odd
            res.append(0)  # Add 0 to the result list

        for i in range(1, mid + 1):  # Iterate from 1 to mid
            res.append(-i)  # Add the negative of i to the result list
            res.append(i)  # Add i to the result list

        return res  

        



        
