class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"(":")","{":"}","[":"]"}

        for symbol in s :
            if symbol in map :
                stack.append(symbol)

            else :
                if not stack :
                    return False

                top =  stack .pop()
                if map[top] != symbol :
                    return False 

        return len(stack) == 0 
                

            

            
                





