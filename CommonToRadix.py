# Python 3.9.0

# CommonToRadix

def CommonToRadix(Common, Base):

    
    '''
    Function requirements:
    Programmer's modules:
    1. BaseNIntegerToBaseTenInteger,
    2. BaseTenRadixToBaseNRadix
    2.1. BaseTenIntegerToBaseNInteger
    2.2. EFormatToRadix
    Parameter requirements:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
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
    if Numerator == '0' and Denominator == '0':
        Fraction = 0.0
    else:
        Fraction = int(Numerator) / int(Denominator)
    Radix = str(int(Whole) + Fraction)
    if Base != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, Base)
    return Radix


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    from BaseTenRadixToBaseNRadix import BaseTenRadixToBaseNRadix
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    from EFormatToRadix import EFormatToRadix
    class I():
        CommonToRadix = CommonToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        EFormatToRadix = EFormatToRadix
    builtins.I = I
    Common = input('Enter Common: ')
    Base = input('Enter Base: ')
    Radix = I.CommonToRadix(Common, Base)
    print(Radix)

        
