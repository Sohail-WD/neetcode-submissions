class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 1

        if not nums:
            return 0

        for num in numsSet:
            current_sequence = 1
            if num - 1 not in numsSet:
                current_num = num
                while current_num + 1 in numsSet:
                    current_num += 1
                    current_sequence += 1

                longest = max(current_sequence,longest)

                
        return longest
                


        
        
        