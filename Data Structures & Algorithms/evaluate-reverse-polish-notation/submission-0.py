class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "add" : "+",
            "sub" : "-",
            "mul" : "*",
            "div" : "/"
        }
        for n in tokens:
            if n in operators.values():
                y = stack.pop()
                x = stack.pop()
                if n == "+":
                    result = x + y
                elif n == "-":
                    result = x-y
                elif n == "*":
                    result = x*y
                else:
                    result = int(x/y)

                stack.append(result)
                           
            else:
                stack.append(int(n))

        return stack[0]
               

                
            
        


















#so,the pattern looks something like this:only after the first two elements will we 
#get to see an operand and after that after every element we will get to see an operand
#which we will have to correspondingly operate with the first elements after their
#operation....this was my initial assumption,however when I looked into leetcode example
#I got to know that operand can alsoe xist after 3 elements aw...atp I am just confused
#as to how it works cuz it math and not just an algorithm that exists.Although I think
#it should work like this:just like stack LIFO,the last two elements get evaluated first
#with the last operand and then the other last 3rd integer with the first two along with 
#the second last operand...ig this is how it works

#also when you divide you can an integer value not a floating value.so use // not /