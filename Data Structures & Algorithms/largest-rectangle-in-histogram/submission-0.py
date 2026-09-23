class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n):
            current_height = heights[i]

            while stack and current_height < stack[-1][1]:
                index, height = stack.pop()
                if stack:
                    width = i - stack[-1][0] - 1
                else:
                    width = i

                area = height * width
                max_area = max(area,max_area)
            stack.append((i,current_height))

        while stack:
            index,height = stack.pop()
            if stack:
                width = n - stack[-1][0] - 1
            else:
                width = n

            area = height * width
            max_area = max(area,max_area)

            

        return max_area

                
