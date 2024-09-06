


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        l = len(s)
        if l < 1: 
            return 0

        curr, result, oper = 0, 0, "+"
        stack = []

        for i, v in enumerate(s):
            if v.isdigit():
                curr = curr * 10 + int(v)

            if i == l - 1 or (not v.isdigit()):
                if oper == "+":
                    stack.append(curr)
                elif oper == "-":
                    stack.append(-curr)
                elif oper == "*":
                    stack.append(stack.pop() * curr)
                elif oper == "/":
                    last = stack.pop()
                    if last // curr < 0 and last % curr != 0:  # Handle negative division
                        stack.append(last // curr + 1)
                    else:
                        stack.append(last // curr)
                
                oper = v
                curr = 0
        
        while stack:
            result += stack.pop()

        return result

