# Python 3.9.0

# SimplifyCommon

def SimplifyCommon(Common, Base):

    
    '''
    Function requirements:
    Programmer's module/s:
    1. BaseNIntegerToBaseTenInteger
    2. BaseTenIntegerToBaseNInteger
    Parameter requirements:
    Common: must be a string common ('n:n|n') with a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    Divisor: must be a string integer.
    '''

    
    IndexOfColon = Common.index(':')
    Whole = Common[:IndexOfColon]
    Fraction = Common[(IndexOfColon + 1):]
    IndexOfBar = Fraction.index('|')
    Numerator = Fraction[:IndexOfBar]
    Denominator = Fraction[(IndexOfBar + 1):]
    if Base != '10':
        Whole = I.BaseNIntegerToBaseTenInteger(Whole, Base)
        Numerator = I.BaseNIntegerToBaseTenInteger(Numerator, Base)
        Denominator = I.BaseNIntegerToBaseTenInteger(Denominator, Base)
    Whole = int(Whole)
    Numerator = int(Numerator)
    Denominator = int(Denominator)
    Divisor = 2
    GoodToGo = 'No'
    while GoodToGo == 'No':
        if Divisor <= Numerator:
            if Numerator % Divisor == 0 and Denominator % Divisor == 0:
                Numerator /= Divisor
                Denominator /= Divisor
            else:
                Divisor += 1
        else:
            GoodToGo = 'Yes'
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(Numerator, Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(Denominator, Base)
    else:
        Whole = int(Whole)
        Numerator = int(Numerator)
        Denominator = int(Denominator)
    Common = f'{Whole}:{Numerator}|{Denominator}'
    return Common


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    class I():
        SimplifyCommon = SimplifyCommon
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
    builtins.I = I
    Common = input('Enter Common: ')
    Base = input('Enter Base: ')
    Common = I.SimplifyCommon(Common, Base)
    print(Common)


