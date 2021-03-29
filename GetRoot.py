# Python 3.9.0

# GetRoot

def GetRoot(Power, Exponent):


    '''
    Parameters:
    Power: must be a literal float.
    Exponent: must be a literal integer.

    Modules:
    Programmer's:
    1. RoundUpOrTruncate
    1.1. EFormatToRadix
    1.1.1. BaseNIntegerToBaseTenInteger
    '''


    Quantity = 1.0
    PreviousWorkingRoot = 0
    WorkingRoot = 1.0
    WorkingPower = 1.0
    Root = 0
    while WorkingPower != Power:
        for Times in range(Exponent - 1):
            WorkingPower *= WorkingRoot
        WorkingPower = I.RoundUpOrTruncate(WorkingPower)
        if WorkingPower == Power:
            Root = WorkingRoot
        elif WorkingPower < Power:
            PreviousWorkingRoot = WorkingRoot
            WorkingRoot += Quantity
            WorkingPower = WorkingRoot
        else:
            Quantity /= 10.0
            WorkingRoot = (PreviousWorkingRoot + Quantity)
            WorkingPower = WorkingRoot
    return Root


if __name__ == '__main__':
    import builtins
    # Programmer's modules:
    from RoundUpOrTruncate import RoundUpOrTruncate
    from EFormatToRadix import EFormatToRadix
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    class I():
        GetRoot = GetRoot
        RoundUpOrTruncate = RoundUpOrTruncate
        EFormatToRadix = EFormatToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
    builtins.I = I
    Power = float(input('Enter Power: '))
    Exponent = int(input('Enter Exponent: '))
    Root = I.GetRoot(Power, Exponent)
    print(Root)
