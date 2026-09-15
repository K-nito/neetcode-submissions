class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []

        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                numStack.append(int(i))
            else:
                num1 = numStack.pop()
                num2 = numStack.pop()

                if i == "+":
                    subRes = num2 + num1
                elif i == "-":
                    subRes = num2 - num1
                elif i == "*":
                    subRes = num2 * num1
                else:
                    subRes = int(num2 / num1)

                numStack.append(subRes)

        return int(numStack[-1])