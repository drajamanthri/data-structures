from collections import deque

class Expression:
    '''
    @param exp:str Mathematical expression.
    '''
    def __init__(self, exp:str):
        self.exp:str = exp

    '''
    This function validate if the expression given by the constructor is has balanced parenthesis.
    '''
    def validate_parenthesis(self)->bool:
        stack = deque()
        for i in range(len(self.exp)):
            token = self.exp[i]

            if token == '(':
                stack.append('(')
            elif token == ')':
                #if the token is ), then the top token on the stack must be a (.
                if stack:
                    top_token = stack[-1]
                    if top_token == '(':
                        #if the top token is (, there are matching opening and closing parenthesis. 
                        #therefore, the opening parenthesis has to be removed from the stack.
                        stack.pop()
                    else:
                        #if the top token is not a (, then the parenthesis are not balanced.
                        return False
                else:
                    #if the stack is empty, parenthesis are not balanced.
                    return False
                
        #if the parenthesis are balanced, at the end, the stack must be empty
        if stack:
            return False
        else:
            return True

expression = Expression('5+4/(1+1)(')
print(expression.validate_parenthesis())
