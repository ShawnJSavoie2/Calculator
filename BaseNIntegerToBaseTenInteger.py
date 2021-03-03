# Python 3.9.0

# BaseNIntegerToBaseTenInteger

def BaseNIntegerToBaseTenInteger(Integer, Base):

    
    '''
    Parameter requirements:
    Integer: must be a string integer that's in a base between and including
    2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''

    
    AlternativeDigits = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
        }
    IntegerList = []
    for Element in Integer:
        if Element in AlternativeDigits:
            IntegerList.append(AlternativeDigits[Element])
        else:
            IntegerList.append(Element)
    PositiveMagnitudes = []
    for Exponent in range(len(IntegerList)):
        Magnitude = int(Base) ** Exponent
        PositiveMagnitudes.append(Magnitude)
    PositiveMagnitudes.reverse()
    Integer = 0
    for Index in range(len(PositiveMagnitudes)):
        Integer += (int(IntegerList[Index]) * PositiveMagnitudes[Index])
    return str(Integer)


if __name__ == '__main__':
    import builtins
    class I():
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
    builtins.I = I
    Integer = input('Enter Integer: ')
    Base = input('Enter Base: ')
    Integer = I.BaseNIntegerToBaseTenInteger(Integer, Base)
    print(Integer)
