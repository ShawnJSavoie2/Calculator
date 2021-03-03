# Python 3.9.0

# ParseExpression


def ParseExpression(Expression, Fraction, Base):

    
    '''
    Function requirements:
    Programmer's module/s:
    1. Radix
    2. Common
    3. CommonToRadix
    3.1 BaseNIntegerToBaseTenInteger,
    3.2 BaseTenRadixToBaseNRadix
    3.2.1 BaseTenIntegerToBaseNInteger
    3.2.2 EFormatToRadix
    4. BaseNRadixToBaseTenRadix
    Parameter requirements:
    Expression: must be a string expression containing only elements from DigitsPointBar,
    SeperatorsAndSpace and OperatorsAndParentheses.
    Fraction: must be a string term: Radix or Common.
    Base: must be a string integer that's one number that's between and including 2 and 16.
    '''

    
    DigitsPointBar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
                      '.', ':', '|']
    SeparatorsAndSpace = [',', '_', ' ']
    OperatorsAndParentheses = ['+', '-', '×', '÷', '˄', '˅', 'T', '(', ')']
    Number = ''
    ExpressionList = []
    for Element in enumerate(Expression):
        if Element[1] in SeparatorsAndSpace:
            continue
        if Element[1] in OperatorsAndParentheses:
            if Expression[(Element[0] - 1)] == 'e':
                Number = f'{Number}{Element[1]}'
            elif Expression[(Element[0] + 1)] in DigitsPointBar:
                if Number != '':
                    ExpressionList.append(Number)
                    Number = Element[1]
                else:
                    Number = Element[1]
            else:
                if Number != '':
                    ExpressionList.append(Number)
                    ExpressionList.append(Element[1])
                    Number = ''
                else:
                    ExpressionList.append(Element[1])
        else:
            Number = f'{Number}{Element[1]}'
    # In case for loop ends before adding.
    if Number != '': 
        ExpressionList.append(Number)
    if Fraction == 'Rad':
        WorkingExpressionList = []
        WorkingNumber = ''
        for Element in ExpressionList:
            if Element in OperatorsAndParentheses:
                WorkingExpressionList.append(Element)
            else:
                if 'e' in Element:
                    WorkingNumber = I.EFormatToRadix(Element, Base)
                    WorkingExpressionList.append(WorkingNumber)
                else:
                    WorkingNumber = I.Radix(Element)
                    WorkingExpressionList.append(WorkingNumber)
        ExpressionList = WorkingExpressionList
    else: # Fraction == 'Com'
        WorkingExpressionList = []
        WorkingNumber = ''
        for Element in ExpressionList:
            if Element in OperatorsAndParentheses:
                WorkingExpressionList.append(Element)
            else:
                WorkingNumber = I.Common(Element)
                WorkingNumber = I.CommonToRadix(WorkingNumber, Base)
                WorkingExpressionList.append(WorkingNumber)
        ExpressionList = WorkingExpressionList
    if Base != '10':
        WorkingExpressionList = []
        WorkingNumber = ''
        for Element in ExpressionList:
            if Element in OperatorsAndParentheses:
                WorkingExpressionList.append(Element)
            else:
                WorkingNumber = I.BaseNRadixToBaseTenRadix(Element, Base)
                WorkingExpressionList.append(WorkingNumber)
        ExpressionList = WorkingExpressionList
    return ExpressionList


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from Radix import Radix
    from Common import Common
    from CommonToRadix import CommonToRadix
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    from BaseTenRadixToBaseNRadix import BaseTenRadixToBaseNRadix
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    from EFormatToRadix import EFormatToRadix
    from BaseNRadixToBaseTenRadix import BaseNRadixToBaseTenRadix
    class I ():
        ParseExpression = ParseExpression
        Radix = Radix
        Common = Common
        CommonToRadix = CommonToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        EFormatToRadix = EFormatToRadix
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
    builtins.I = I
    Expression = input('Enter Expression: ')
    Fraction = input('Enter Fraction: ')
    Base = input('Enter Base: ')
    ExpressionList = I.ParseExpression(Expression, Fraction, Base)
    print(ExpressionList)
