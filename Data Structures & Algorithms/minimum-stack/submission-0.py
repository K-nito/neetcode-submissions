class MinStack:
    #Create a stack for the main elements, and a stack for the minimun element hierarchy
    mainStack = []
    PFStack = []

    def __init__(self):
        self.mainStack = []
        self.PFStack = []

    def push(self, val: int) -> None:
        #push val to mainstack, but push the minimum b/w val and PFStack top element if PFStack isn't empty
        self.mainStack.append(val)
        self.PFStack.append(min(val, self.PFStack[-1])) if self.PFStack else self.PFStack.append(val)

    def pop(self) -> None:
        #Pop elements from both stacks
        self.mainStack.pop()
        self.PFStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.PFStack[-1]
        
