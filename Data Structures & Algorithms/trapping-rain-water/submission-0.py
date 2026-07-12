class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0 
            
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        leftMax[0] = height[0]
        rightMax[len(height) - 1] = height[len(height) - 1]
        output = 0

        for i in range(1,len(height)):
            leftMax[i] = max(leftMax[i-1],height[i])
        
        for i in range(len(height) - 2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])

        for i in range(len(leftMax)):
            water = min(leftMax[i],rightMax[i]) - height[i]
            output += max(water,0)

       

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
