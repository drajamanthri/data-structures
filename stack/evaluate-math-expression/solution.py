from collections import deque

class Expression:
    def __init__(self, expression:str):
        self.exp:str = expression
        self.operators:list = ['+', '-', '*', '/']
        self.precedence:dict = {'+': 0, '-': 0, '*': 1, '/': 1}

    def eval(self):
        vals = deque() #vals stack
        ops = deque()

        for i in range(0, len(self.exp)):
            #first we want to separate out operators and operands into two stacks.
            token = self.exp[i]
            if token.isnumeric():
                #if the token is a number, add it to the vals stack
                vals.append(token)
            elif self.tokenIsOperator(token):
                #if the token is an operator
                if len(ops) == 0:
                    #if the operator stack is empty, add the token to the operator stack
                    ops.append(token)
                else:
                    #if the operator stack is not empty
                    last_op = ops[-1]
                    while ops and (not self.higher_precedence(token, last_op)):
                        #while the current operand does not have a higher precedence, apply the stacked operators.
                        last_op = ops.pop()
                        val2 = vals.pop()
                        val1 = vals.pop()
                        result = self.apply_operator(last_op, val1, val2)
                        vals.append(result)
                        if ops:
                            last_op = ops[-1]

                    #add the current operand
                    ops.append(token)

        #finally apply the stacked operators
        while ops:
            op = ops.pop()
            val2 = vals.pop()
            val1 = vals.pop()
            result = self.apply_operator(op, val1, val2)
            vals.append(result)

        return vals.pop()
    
    def tokenIsOperator(self, token)->bool:
        if token in self.operators:
            return True
        else:
            return False
    '''
    @param operator1:str current operator
    @param operator2:str current operator
    @return bool True if operator 1 has higher precedence than operator 2
    '''
    def higher_precedence(self, operator1:str, operator2:str)->bool:
        if self.precedence[operator1] > self.precedence[operator2]:
            return True
        else:
            return False
        
    def apply_operator(self, operator:str, operand1:str, operand2:str)->int:
        if operator == '+':
            return int(operand1) + int(operand2)
        elif operator == '-':
            return int(operand1) - int(operand2)
        elif operator == '*':
            return int(operand1) * int(operand2)
        elif operator == '/':
            return int(operand1) / int(operand2)
        
expression = Expression('2+3+4')
result = expression.eval()
print(result)
