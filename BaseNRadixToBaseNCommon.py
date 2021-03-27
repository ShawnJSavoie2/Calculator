# Python 3.9.0

# BaseNRadixToBaseNCommon

def BaseNRadixToBaseNCommon(Radix, FromBase, ToBase):


    '''
    Function requirements:
    Programmer's modules:
    1. Radix
    2. BaseNRadixToBaseTenRadix
    3. BaseTenRadixToBaseNRadix
    3.1. BaseTenIntegerToBaseNInteger
    3.2. EFormatToRadix
    3.2.1. BaseNIntegerToBaseTenInteger
    4. RadixToCommon
    4.1. RoundUpOrTruncate
    4.2 SimplifyCommon
    5. FormatNumber
    Parameter requirements:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.
    '''


    Radix = I.Radix(Radix)
    Separators = [',', '_']
    Number = ''
    for Element in Radix:
        if Element in Separators:
            continue
        else:
            Number = f'{Number}{Element}'
    Radix = Number
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    Common = I.RadixToCommon(Radix, ToBase)
    Common = I.FormatNumber(Common)
    return Common


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from Radix import Radix
    from BaseNRadixToBaseTenRadix import BaseNRadixToBaseTenRadix
    from BaseTenRadixToBaseNRadix import BaseTenRadixToBaseNRadix
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    from EFormatToRadix import EFormatToRadix
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    from RadixToCommon import RadixToCommon
    from RoundUpOrTruncate import RoundUpOrTruncate
    from SimplifyCommon import SimplifyCommon
    from FormatNumber import FormatNumber
    class I():
        BaseNRadixToBaseNCommon = BaseNRadixToBaseNCommon
        Radix = Radix
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        EFormatToRadix = EFormatToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        RadixToCommon = RadixToCommon
        RoundUpOrTruncate = RoundUpOrTruncate
        SimplifyCommon = SimplifyCommon
        FormatNumber = FormatNumber
    builtins.I = I
    Radix = input('Enter Radix: ')
    FromBase = input('Enter FromBase: ')
    ToBase = input('Enter ToBase: ')
    Common = I.BaseNRadixToBaseNCommon(Radix, FromBase, ToBase)
    print(Common)
