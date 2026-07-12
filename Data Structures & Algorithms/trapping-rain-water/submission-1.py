class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
    

        left = 0
        right = len(height) - 1
        output = 0 
        water = 0

        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            
            if leftMax <= rightMax:
                water = leftMax - height[left]
                output += max(water,0)
                left += 1
                leftMax = max(leftMax, height[left])


            else:
                water = rightMax - height[right]
                output += max(water,0)
                right -= 1
                rightMax = max(rightMax,height[right])

        return output



        

        


        

        
#the idea here is that if there are two integers i and j,and in between is 0 then water
#trapped is the minimum of those...and in the case of there being no 0 in between 
#and two equal integers like say 3 and 3 ...then we will have to subtract the numbers 
#after them from 3 each time like 3-1,3-0...and then add it to a variable lets say result

#apart from that,if the difference between two consecutive bars is 1 ,then it is not 
#possible to store water there(0 is the onlly exception,meaning if there is a 0 and 
#a 1,then we can still store 1 unit of water).

#most importantly,the wrong idea here is in order to store water,bar height must be 0 between two bars
#I understood this after looking at the same problem on leetcode with example.
