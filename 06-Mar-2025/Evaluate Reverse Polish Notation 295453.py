# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # evaluation of strings
        stack = []
        for num in range(len(tokens)):
            if tokens[num] in "+-*/":
                nums= tokens[num]
                
                temp1 = stack.pop()
                temp1 = int(temp1)
                temp2 = stack.pop()
                temp2 =int(temp2)
                if nums == "+":
                    ans = temp2 + temp1
                elif nums == "*":
                    ans = temp2 * temp1
                elif nums == "/":
                    ans = int(temp2 / temp1)
                else:
                    ans = temp2 - temp1
                stack.append(ans)
            else:
                stack.append(int(tokens[num]))
                
        return stack[0]
