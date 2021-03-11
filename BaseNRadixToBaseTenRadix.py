# Python 3.9.0

# BaseNRadixToBaseTenRadix

def BaseNRadixToBaseTenRadix(Radix, Base):


    '''
    Parameter requirements:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    '''


    AlternativeDigits = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
        }
    RadixList = []
    for Element in Radix:
        if Element in AlternativeDigits:
            RadixList.append(AlternativeDigits[Element])
        else:
            RadixList.append(Element)
    IndexOfPoint = RadixList.index('.')
    Whole = RadixList[:IndexOfPoint]
    Fraction = RadixList[(IndexOfPoint + 1):]
    # Whole part.
    PositiveMagnitudes = []
    for Exponent in range(len(Whole)):
        Magnitude = int(Base) ** Exponent
        PositiveMagnitudes.append(Magnitude)
    PositiveMagnitudes.reverse()
    ConvertedWhole = 0
    for Index in range(len(PositiveMagnitudes)):
        ConvertedWhole += (float(Whole[Index]) * PositiveMagnitudes[Index])
    # Fraction part
    NegativeMagnitudes = []
    for Exponent in range(len(Fraction) + 1):
        if Exponent == 0:
            continue
        Magnitude = 1 / (int(Base) ** Exponent)
        NegativeMagnitudes.append(Magnitude)
    ConvertedFraction = 0
    for Index in range(len(NegativeMagnitudes)):
        ConvertedFraction += (float(Fraction[Index]) * NegativeMagnitudes[Index])
    # Whole and fraction parts.
    Radix = str(ConvertedWhole + ConvertedFraction)
    return Radix


if __name__ == '__main__':
    import builtins
    class I():
        BaseNRadixToBaseTenRadix = BaseNRadixToBaseTenRadix
    builtins.I = I
    Radix = input('Enter Radix: ')
    Base = input('Enter Base: ')
    Radix = I.BaseNRadixToBaseTenRadix(Radix, Base)
    print(Radix)
