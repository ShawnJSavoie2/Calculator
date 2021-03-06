# Python 3.9.0

# BaseNCommonToBaseNCommon

def BaseNCommonToBaseNCommon(Common, FromBase, ToBase):


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
    4. RadixToCommon
    4.1. RoundUpOrTruncate
    4.2. SimplifyCommon
    5. FormatNumber
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
    Common = I.RadixToCommon(Radix, ToBase)
    Common = I.FormatNumber(Common)
    return Common


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
    from RadixToCommon import RadixToCommon
    from RoundUpOrTruncate import RoundUpOrTruncate
    from SimplifyCommon import SimplifyCommon
    from FormatNumber import FormatNumber
    class I():
        BaseNCommonToBaseNCommon = BaseNCommonToBaseNCommon
        Common = Common
        CommonToRadix = CommonToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        EFormatToRadix = EFormatToRadix
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
        RadixToCommon = RadixToCommon
        RoundUpOrTruncate = RoundUpOrTruncate
        SimplifyCommon = SimplifyCommon
        FormatNumber = FormatNumber
    builtins.I = I
    Common = input('Enter Common: ')
    FromBase = input('Enter FromBase: ')
    ToBase = input('Enter ToBase: ')
    Common = I.BaseNCommonToBaseNCommon(Common, FromBase, ToBase)
    print(Common)
