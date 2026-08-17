class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        needed = None
        i =0 

        for num in nums:
            needed = target - num

            if needed in seen:
                return [seen[needed],i]
            
            seen[num] = i
            i += 1

        

        
        

        