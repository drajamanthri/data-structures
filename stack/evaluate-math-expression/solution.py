from collections import deque

'''
This class represents a mathematical expression. The expression is given as a string when creating an
object of the Expression class.
This algorithm evaluate expression without first converting the expression into post fix.
'''
class Expression:
    def __init__(self, expression:str):
        self.exp:str = expression
        self.operators:list = ['+', '-', '*', '/']
        self.precedence:dict = {'+': 0, '-': 0, '*': 1, '/': 1}

    '''
    This function evaluate the expression given by the constructor
    '''
    def eval(self):
        vals = deque() #vals stack
        ops = deque()

        for i in range(0, len(self.exp)):
            #first we want to separate out operators and operands into two stacks.
            token = self.exp[i]
            if token.isnumeric():
                #if the token is a number, add it to the vals stack
                vals.append(token)
            elif token == '(':
                # if the token is the left parenthesis push it to ops
                ops.append(token)
            elif token == ')':
                last_op = ops[-1]
                while ops and last_op != '(':
                    op = ops.pop()
                    val2 = vals.pop()
                    val1 = vals.pop()
                    result = self.apply_operator(op, val1, val2)
                    vals.append(result)
                    if ops:
                        last_op = ops[-1]

                if ops and last_op == '(':
                    ops.pop()

            elif self.tokenIsOperator(token):
                #if the token is an operator
                if len(ops) == 0:
                    #if the operator stack is empty, add the token to the operator stack
                    ops.append(token)
                else:
                    #if the operator stack is not empty
                    last_op = ops[-1]
                    while ops and last_op != '(' and (not self.higher_precedence(token, last_op)):
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
        
    '''
    @param operator:str +, -, *, /
    @param operand1:str 
    @param operand2:str
    for example 
    operand1 + operand2
    '''    
    def apply_operator(self, operator:str, operand1:str, operand2:str)->int:
        if operator == '+':
            return int(operand1) + int(operand2)
        elif operator == '-':
            return int(operand1) - int(operand2)
        elif operator == '*':
            return int(operand1) * int(operand2)
        elif operator == '/':
            return int(operand1) // int(operand2)
        
expression = Expression('5+4/(1+1)')
result = expression.eval()
print(result)
