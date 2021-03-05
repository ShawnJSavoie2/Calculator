# Python 3.9.0

# Calculate

def Calculate(ExpressionList):


    '''
    Parameter requirements:
    ExpressionList: must be a list containing at least two string floats and one string operator.
    '''


    Operators = ['+', '-', '×', '÷', '˄', '˅', 'T']
    OperatorsAndParentheses = ['+', '-', '×', '÷', '˄', '˅', 'T', '(', ')']
    OperandOne = ''
    Operator = ''
    OperandTwo = ''
    ForIndex = 0
    for Element in ExpressionList:
        if Element not in OperatorsAndParentheses:
            if OperandOne == '':
                OperandOne = Element
            else:
                OperandTwo = Element
        if Element in Operators:
            Operator = Element
        if Element == '(':
            Result = I.Calculate(ExpressionList[(ForIndex + 1):])
            if OperandOne == '':
                OperandOne = Result
            else:
                OperandTwo = Result
            GoodToGo = 'no'
            LeftParentheses = 0
            RightParentheses = 0
            WhileIndex = ForIndex
            while GoodToGo == 'no':
                if ExpressionList[WhileIndex] == '(':
                    LeftParentheses = LeftParentheses + 1
                if ExpressionList[WhileIndex] == ')':
                    RightParentheses = RightParentheses + 1
                ExpressionList[WhileIndex] = ''
                if LeftParentheses != RightParentheses:
                    GoodToGo = 'no'
                    WhileIndex = WhileIndex + 1
                else:
                    GoodToGo = 'yes'
        if Element == ')':
            return OperandOne
        if OperandOne != '' and Operator != '' and OperandTwo != '':
            if Operator == '+':
                OperandOne = float(OperandOne) + float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '-':
                OperandOne = float(OperandOne) - float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '×':
                OperandOne = float(OperandOne) * float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '÷':
                OperandOne = float(OperandOne) / float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '˄':
                OperandOne = float(OperandOne) ** float(OperandTwo)
                Operator = ''
                OperandTwo = ''
            elif Operator == '˅':
                OperandOne = float(OperandOne) ** (1 / float(OperandTwo))
                Operator = ''
                OperandTwo = ''
            elif Operator == 'T':
                OperandOne = float(I.GetExponent(float(OperandOne), float(OperandTwo)))
                Operator = ''
                OperandTwo = ''
        ForIndex = ForIndex + 1
    return str(OperandOne)


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from GetExponent import GetExponent
    class I():
        Calculate = Calculate
        GetExponent = GetExponent
    builtins.I = I
    # Test function below:
    '''
    ExpressionList = # <<---- Make a list with at least two string floats and one string operator.
    OperandOne = I.Calculate(ExpressionList)
    print(OperandOne)
    '''
