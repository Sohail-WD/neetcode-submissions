class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
            
               

        

        
        
#the idea is to have closed brackets for every opening bracket in such a way:
#we will have two pointers left and right again...if left == right then we can move
#left+=1 and right-=1 and if not then return false....so now this ensures that brackets 
#are closed in the correct order