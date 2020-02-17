class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = list()
        for i in A:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
                continue
            right = int(stack.pop())
            left = int(stack.pop())
            if i == '+':
                res = left + right
            elif i == '-':
                res = left - right
            elif i == '*':
                res = left * right
            elif i == '/':
                res = left / right
            stack.append(res)
        return stack.pop()
