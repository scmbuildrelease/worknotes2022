class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for i, c in enumerate(s):
            if c =="(":
                stack.append(i)
            elif c==")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        while stack:
            to_remove.add(stack.pop())
        result=[]
        for i, c in enumerate(s):
            if i not in to_remove:
                result.append(c)
        return "".join(result)  
            
        
