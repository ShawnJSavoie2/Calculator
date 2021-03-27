# Python 3.9.0

# RoundUpOrTruncate

def RoundUpOrTruncate(Radix):


    '''
    Parameters:
    Radix: must be a literal float.

    Modules:
    Programmer's:
    1. EFormatToRadix
    1.1. BaseNIntegerToBaseTenInteger
    '''


    Radix = str(Radix)
    if 'e' in Radix:
        Radix = I.EFormatToRadix(Radix, Base)
    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    LengthOfFraction = len(Fraction)
    Count = 0
    for Digit in Fraction:
        if Digit == '0':
            Count += 1
        else:
            break
    if Count >= 4:
        if Count == LengthOfFraction or Count == (LengthOfFraction - 1):
            Radix = float(Whole)
            return Radix
    else:
        Count = 0
    for Element in Fraction:
        if Element == '9':
            Count += 1
        else:
            break
    if Count >= 4:
        if Count == LengthOfFraction or Count == (LengthOfFraction - 1):
            Radix = float(Whole) + 1
            return Radix
    return float(Radix)


if __name__ == '__main__':
    import builtins
    # Programmer's module/s
    from EFormatToRadix import EFormatToRadix
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    class I():
        RoundUpOrTruncate = RoundUpOrTruncate
        EFormatToRadix = EFormatToRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
    builtins.I = I
    Radix = input('Enter Radix: ')
    Radix = I.RoundUpOrTruncate(Radix)
    print(Radix)
