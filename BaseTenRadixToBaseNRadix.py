# Python 3.9.0

# BaseTenRadixToBaseNRadix

def BaseTenRadixToBaseNRadix(Radix, Base):


    '''
    Function requirements:
    Programmer's modules:
    1. BaseTenIntegerToBaseNInteger
    Parameter requirements:
    Radix: must be a string radix that's in base 10.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    Whole = int(Whole)
    Base = int(Base)
    if Whole != 0:
        Exponent = 1
        Magnitude = Base ** Exponent
        while Whole > Magnitude:
            Exponent = Exponent + 1
            Magnitude = Base ** Exponent
        if Magnitude > Whole:
            Magnitude = Magnitude / Base
            Exponent = Exponent - 1
        Digits = []
        Digit = Whole // Magnitude
        Remainder = Whole - (Digit * Magnitude)
        Digits.append(int(Digit))
        if Exponent != 0:
            Magnitude = Magnitude / Base
            Exponent = Exponent - 1
            if Remainder >= Base:
                GoodToGo = 'no'
                while GoodToGo == 'no':
                    if Magnitude > Remainder:
                        Digits.append(0)
                        Magnitude = Magnitude / Base
                        Exponent = Exponent - 1
                    else: # Magnitude < Remainder
                        Digit = Remainder // Magnitude
                        Remainder = Remainder - (Digit * Magnitude)
                        Digits.append(int(Digit))
                        Magnitude = Magnitude / Base
                        Exponent = Exponent - 1
                    if Remainder >= Base:
                        GoodToGo = 'no'
                    else:
                        GoodToGo = 'yes'
            if Exponent != 0:
                for Count in range(Exponent):
                    Digits.append(0)
            Digits.append(int(Remainder))
        AlternativeDigits = {
            '10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F'
            }
        Whole = ''
        for Digit in Digits:
            if str(Digit) in AlternativeDigits:
                Whole = f'{Whole}{AlternativeDigits[str(Digit)]}'
            else:
                Whole = f'{Whole}{Digit}'
    #Fraction part
    if Fraction != '0':
        Exponent = 1
        for Digit in Fraction:
            if Digit == '0':
                Exponent = Exponent + 1
            else:
                break
        Fraction = f'.{Fraction}'
        Divisor = (10 ** Exponent) / (float(Fraction) * (10 ** Exponent))
        Exponent = 1
        Magnitude = Base ** Exponent
        while Divisor > Magnitude:
            Exponent = Exponent + 1
            Magnitude = Base ** Exponent
        Quotient = Magnitude / Divisor
        Fraction = ''
        if (Quotient % 1) == 0:
            Fraction = str(int(Quotient))
        else:
            for Element in str(Quotient):
                if Element != '.':
                    Fraction = f'{Fraction}{Element}'
        Fraction = I.BaseTenIntegerToBaseNInteger(Fraction, Base)
        if Fraction[-1] == '0':
            while Fraction[-1] == '0':
                Fraction = Fraction[:-1]
        if Exponent != 0:
            for Count in range(Exponent - 1):
                Fraction = f'0{Fraction}'
    # Whole and Fraction parts
    Radix = f'{Whole}.{Fraction}'
    return Radix


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from BaseTenIntegerToBaseNInteger import BaseTenIntegerToBaseNInteger
    class I():
        BaseTenRadixToBaseNRadix = BaseTenRadixToBaseNRadix
        BaseTenIntegerToBaseNInteger = BaseTenIntegerToBaseNInteger
    builtins.I = I
    Radix = input('Enter Radix: ')
    Base = input('Enter Base: ')
    Radix = I.BaseTenRadixToBaseNRadix(Radix, Base)
    print(Radix)
