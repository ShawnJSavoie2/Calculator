# Python 3.9.0

# RadixToCommon

def RadixToCommon(Radix, Base):

    
    '''
    Function requirements:
    Programmer's module/s:
    1. BaseNRadixToBaseTenRadix,
    2. RoundUpOrTruncate
    2.1. EFormatToRadix
    2.1.1. BaseNIntegerToBaseTenInteger
    3. BaseTenIntegerToBaseNInteger
    4. SimplifyCommon 
    Parameter requirements:
    Radix: must be a string radix with a base that's between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''

    
    if Base != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[IndexOfPoint:]
    Denominator = 2
    GoodToGo = 'No'
    while GoodToGo == 'No': 
        Numerator = float(Fraction) * Denominator
        if Numerator % 1 == 0:
            GoodToGo = 'Yes'
        else:
            Numerator = I.RoundUpOrTruncate(Numerator)
            if Numerator % 1 == 0:
                GoodToGo = 'Yes'
            else:
                Denominator += 1
    if Base != '10':
        Whole = I.BaseTenIntegerToBaseNInteger(Whole, Base)
        Numerator = I.BaseTenIntegerToBaseNInteger(str(int(Numerator)), Base)
        Denominator = I.BaseTenIntegerToBaseNInteger(str(Denominator), Base)
    Whole = int(Whole)
    Numerator = int(Numerator)
    Denominator = int(Denominator)
    if Numerator == 0:
        Denominator = 0
        Common = f'{Whole}:{Numerator}|{Denominator}'
    else:
        Common = f'{Whole}:{Numerator}|{Denominator}'
        Common = I.SimplifyCommon(Common, Base)
    return Common


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from BaseNRadixToBaseTenRadix import BaseNRadixToBaseTenRadix
    from RoundUpOrTruncate import RoundUpOrTruncate
    from EFormatToRadix import EFormatToRadix
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    from SimplifyCommon import SimplifyCommon
    class I():
        RadixToCommon = RadixToCommon
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
        RoundUpOrTruncate = RoundUpOrTruncate
        EFormatToRadix = EFormatToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        SimplifyCommon = SimplifyCommon
    builtins.I = I
    Radix = input('Enter Radix: ')
    Base = input('Enter Base: ')
    Common = I.RadixToCommon(Radix, Base)
    print(Common)
