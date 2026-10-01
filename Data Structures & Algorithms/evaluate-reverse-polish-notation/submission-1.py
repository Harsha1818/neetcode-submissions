class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        map = {
            "+" : lambda a,b :a+b, 
            "-" : lambda a,b : a-b,
            "*" : lambda a,b : a*b,
            "/" : lambda a,b :int(a/b),
        }

        stack = []
        for symbol in tokens :
            if symbol not in map :
                stack.append(int(symbol))

            else :
                a= stack .pop()
                b = stack.pop()
                res = map[symbol](b,a)
                stack.append(res)

        return stack[0]
         
