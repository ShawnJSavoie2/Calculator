# Python 3.9.0

# RadixToEFormat

def RadixToEFormat(Radix, Base):


    '''
    Parameters:
    Radix: must be a string Radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.

    Modules:
    Programmer's:
    1. BaseTenIntegerToBaseNInteger
    2. FormatNumber
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    if Whole == '0':
        Zeros = 0
        for Digit in Fraction:
            if Digit == '0':
                Zeros += 1
            else:
                break
        if Zeros >= 4:
            Exponent = Zeros + 1
            if (len(Fraction) - Zeros) > 1:
                Fraction = f'{Fraction[Zeros]}.{Fraction[(Zeros + 1):]}'
            else:
                Fraction = Fraction[Zeros]
            if Base != '10':
                Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
            Fraction = I.FormatNumber(Fraction)
            EFormat = f'{Fraction}e-{Exponent}'
            return EFormat
    else: # Whole != '0'
        if Fraction == '0':
            Zeros = 0
            for Digit in reversed(Whole):
                if Digit == '0':
                    Zeros += 1
                else:
                    break
            if Zeros >= 4:
                Exponent = len(Whole) - 1
                if (len(Whole) - Zeros) > 1:
                    Whole = f'{Whole[0]}.{Whole[1:-Zeros]}'
                else:
                    Whole = Whole[0]
                if Base != '10':
                    Exponent = I.BaseTenIntegerToBaseNInteger(Exponent, Base)
                Whole = I.FormatNumber(Whole)
                EFormat = f'{Whole}e+{Exponent}'
                return EFormat
    return Radix


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    from FormatNumber import FormatNumber
    class I():
        RadixToEFormat = RadixToEFormat
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
        FormatNumber = FormatNumber
    builtins.I = I
    Radix = input('Enter Radix: ')
    Base = input('Enter Base: ')
    EFormat = I.RadixToEFormat(Radix, Base)
    print(EFormat)
