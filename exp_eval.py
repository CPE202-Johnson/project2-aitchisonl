from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''

    pStack = Stack(30)
    index = 0
    currentChar = ""
    currentStr = ""
    input_str += " "
    operators = ["/", "+", "-", "*", "**"]

    while (index < len(input_str)):
        currentChar = input_str[index]
        if (currentChar == " "): 

            if (currentStr in operators):
                if (pStack.size() >= 2):
                    num1 = pStack.pop()
                    num2 = pStack.pop()
                    op = doOp(currentStr, num1, num2)
                    pStack.push(op)
                else:
                    raise PostfixFormatException("Insufficient operands")
            elif (currentStr.isnumeric()):
                pStack.push(int(currentStr))
            elif isFloat(currentStr):
                pStack.push(float(currentStr))
            else:
                raise PostfixFormatException("Invalid token")

                

            currentStr = ""
        else:
            currentStr += currentChar
        index+= 1
    if (pStack.size() != 1):
        raise PostfixFormatException("Too many operands")
    return (pStack.pop())


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    currentPre = ""
    preStack = Stack(30)
    items = input_str.split(" ")
    operators = ["/", "+", "-", "*", "**"]
    index = 0
    while index < len(items):
        item = items[len(items)-(index+1)]
        if (item in operators):
            num1 = preStack.pop()
            num2 = preStack.pop()
            preStack.push(str(num1)+" "+str(num2)+" "+item)
        else:
            preStack.push(item)
        
        index+= 1
    return preStack.pop()


def doOp(op, num1, num2):
    if (op == "+"):
        return num1+num2
    if (op == "-"):
        return num2-num1
    if (op == "*"):
        return num1*num2
    if (op == "/"):
        if (num2 == 0):
            return 0
        return num2/num1
    if (op == "**"):
        return num2**num1
def isFloat(stri):
    isfl = True
    for char in stri:
        if not char.isnumeric():
            if char != ".":
                if char != "-":
                    isfl = False
    return isfl