# Python 3.9.0

# BaseNCommonToBaseNRadix

def BaseNCommonToBaseNRadix(Common, FromBase, ToBase):

    
    '''
    Function requirements:
    Programmer's modules:
    1. Common
    2. CommonToRadix
    2.1. BaseNIntegerToBaseTenInteger
    2.2. BaseTenRadixToBaseNRadix
    2.2.1. BaseTenIntegerToBaseNInteger
    2.2.2. EFormatToRadix
    3. BaseNRadixToBaseTenRadix
    Parameter requirements:
    Radix: must be a string radix that's in base 10.
    Base: must be a string integer that's one number between and including 2 and 16.
    Parameter requirements:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.
    '''


    Common = I.Common(Common)
    Radix = I.CommonToRadix(Common, FromBase)
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    return Radix


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from Common import Common
    from CommonToRadix import CommonToRadix
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    from BaseTenRadixToBaseNRadix import BaseTenRadixToBaseNRadix
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    from EFormatToRadix import EFormatToRadix
    from BaseNRadixToBaseTenRadix import BaseNRadixToBaseTenRadix
    class I():
        BaseNCommonToBaseNRadix = BaseNCommonToBaseNRadix
        Common = Common
        CommonToRadix = CommonToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        EFormatToRadix = EFormatToRadix
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
    builtins.I = I
    Common = input('Enter Common: ')
    FromBase = input('Enter FromBase: ')
    ToBase = input('Enter ToBase: ')
    Common = I.BaseNCommonToBaseNRadix(Common, FromBase, ToBase)
    print(Common)
