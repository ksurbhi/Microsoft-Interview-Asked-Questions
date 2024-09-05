import heapq

class Solution:
    """
    Time: O(N)
    Space: O(N) [O(N) space for the string storage and for heap space it will be log(3) which is O(1)]
    """
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""  # Initialize the result string
        maxHeap = []  # Create a max-heap to store characters and their counts

        # Add the counts and corresponding characters to the heap
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)  # Get the character with the maximum remaining count
            
            # Check if adding this character would violate the no-three-consecutive constraint
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:  # If the heap is empty, we can't avoid the violation
                    break
                
                # Get the second most frequent character
                count2, char2 = heapq.heappop(maxHeap) 
                
                # Add the second most frequent character to the result
                res += char2
                count2 += 1  # Increment the count (since count is negative, we increment here)

                if count2 != 0:
                    heapq.heappush(maxHeap, (count2, char2))  # Push the updated count back into the heap
            else:
                # Add the most frequent character to the result
                res += char
                count += 1  # Increment the count (since count is negative, we increment here)

            if count != 0:
                heapq.heappush(maxHeap, (count, char))  # Push the updated count back into the heap

        return res
