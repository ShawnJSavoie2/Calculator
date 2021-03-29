# Python 3.9.0

# BaseNCommonToBaseNRadix

def BaseNCommonToBaseNRadix(Common, FromBase, ToBase):


    '''
    Parameters:
    Common: must be a string common ('n:n|n') that's in a base between and including 2 and 16.
    FromBase: must be a string integer that's one number between and including 2 and 16.
    ToBase: must be a string integer that's one number between and including 2 and 16.

    Modules:
    Programmer's:
    1. Common
    2. CommonToRadix
    2.1. BaseNIntegerToBaseTenInteger
    2.2. BaseTenRadixToBaseNRadix
    2.2.1. BaseTenIntegerToBaseNInteger
    2.2.2. EFormatToRadix
    3. BaseNRadixToBaseTenRadix
    4. FormatNumber
    '''


    Common = I.Common(Common)
    Separators = [',', '_']
    WorkingCommon = ''
    for Element in Common:
        if Element in Separators:
            continue
        else:
            WorkingCommon = f'{WorkingCommon}{Element}'
    Common = WorkingCommon
    Radix = I.CommonToRadix(Common, FromBase)
    if FromBase != '10':
        Radix = I.BaseNRadixToBaseTenRadix(Radix, FromBase)
    if ToBase != '10':
        Radix = I.BaseTenRadixToBaseNRadix(Radix, ToBase)
    Radix = I.FormatNumber(Radix)
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
    from FormatNumber import FormatNumber
    class I():
        BaseNCommonToBaseNRadix = BaseNCommonToBaseNRadix
        Common = Common
        CommonToRadix = CommonToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        EFormatToRadix = EFormatToRadix
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
        FormatNumber = FormatNumber
    builtins.I = I
    Common = input('Enter Common: ')
    FromBase = input('Enter FromBase: ')
    ToBase = input('Enter ToBase: ')
    Common = I.BaseNCommonToBaseNRadix(Common, FromBase, ToBase)
    print(Common)
