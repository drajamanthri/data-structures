class Expression:
    def __init__(self, exp):
        self.exp = exp
        self.openings = set(['(', '[', '{'])
        self.closings = {')': '(', ']': '[', '}': '{'}

    def eval(self):
        stack = []
        for c in self.exp:
            if c in self.openings:
                #if the char an opening, push it to the stack
                stack.append(c)
            elif c in self.closings:
                #if the char is a closing, the top char in the stack 
                #should match with it
                if stack:
                    top = stack.pop()

                    if self.closings[c] != top:
                        return False
                else:
                    #if the stack is empty, it's an error
                    return False
        #at the end stack must be empty
        return not stack


exp = Expression('[{()}]') #test by changing the expression
print(exp.eval())