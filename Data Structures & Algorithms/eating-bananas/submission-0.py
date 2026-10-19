class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0

            for pile in piles:
                quotient = pile // mid
                remainder = pile % mid

                if remainder > 0:
                    quotient += 1

                total_hours += quotient

            if total_hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left

    
            

                    
        

        

        
        