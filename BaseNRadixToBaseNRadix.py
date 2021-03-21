# Python 3.9.0

# BaseNRadixToBaseNRadix

def BaseNRadixToBaseNRadix(Radix, FromBase, ToBase):


    '''
    Function requirements:
    Programmer's modules:
    1. Radix
    2. BaseNRadixToBaseTenRadix
    3. BaseTenRadixToBaseNRadix
    3.1. BaseTenIntegerToBaseNInteger
    3.2. EFormatToRadix
    3.2.1. BaseNIntegerToBaseTenInteger
    4. FormatNumber
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
    Radix = I.FormatNumber(Radix)
    return Radix


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from Radix import Radix
    from BaseNRadixToBaseTenRadix import BaseNRadixToBaseTenRadix
    from BaseTenRadixToBaseNRadix import BaseTenRadixToBaseNRadix
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    from EFormatToRadix import EFormatToRadix
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    from FormatNumber import FormatNumber
    class I():
        BaseNRadixToBaseNRadix = BaseNRadixToBaseNRadix
        Radix = Radix
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        EFormatToRadix = EFormatToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        FormatNumber = FormatNumber
    builtins.I = I
    Radix = input('Enter Radix: ')
    FromBase = input('Enter FromBase: ')
    ToBase = input('Enter ToBase: ')
    Radix = I.BaseNRadixToBaseNRadix(Radix, FromBase, ToBase)
    print(Radix)
