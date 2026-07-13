class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack= []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
#for push we can just add the integer value to the stack although we do not return
#anything here
#for pop,we remove the last element of the stack,that is stack[-1]...we dont return
#anything here as well
#for top,we return stack[-1]
#for getMin,we return the minimum element in the stack using min() but I am confused
#since we need to run in O(1) time,how can we optimize it?