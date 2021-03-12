# Python 3.9.0

# RoundRadix

def RoundRadix(Radix, Base, Place):


    '''
    Function requirements:
    Programmer's module/s:
    1. BaseNIntegerToBaseTenInteger
    Parameter requirements:
    Radix: must be a string radix that's in a base between and including 2 and 16.
    Base: must be a string integer that's one number between and including 2 and 16.
    Place: must be a string integer that's in a base equal to the Base.
    '''


    IndexOfPoint = Radix.index('.')
    Whole = Radix[:IndexOfPoint]
    Fraction = Radix[(IndexOfPoint + 1):]
    if Base == '10':
        if len(Fraction) > int(Place):
            Fraction = f'0.{Fraction}'
            Fraction = round(float(Fraction), int(Place))
            Radix = str(float(Whole) + Fraction)
    else:
        Place = I.BaseNIntegerToBaseTenInteger(Place, Base)
        if len(Fraction) > int(Place):
            Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                      'F']
            HalfBase = round(int(Base) / 2)
            UsedDigits = Digits[:int(Base)]
            HalfOfDigits = UsedDigits[:HalfBase]
            FractionList = []
            for Digit in reversed(Fraction):
                FractionList.append(Digit)
            Count = len(Fraction) - int(Place)
            CurrentDigit = FractionList[0]
            for Element in enumerate(FractionList):
                if Count == 0:
                    break
                else:
                    if Count == 1 and FractionList[(Element[0] + 1)] == Digits[int(Base)] or FractionList[(Element[0] + 1)] == Digits[(int(Base) - 1)]:
                        CurrentDigit = FractionList[(Element[0] + 1)]
                        Count -= 1
                    else:
                        if CurrentDigit in HalfOfDigits:
                            CurrentDigit = FractionList[(Element[0] + 1)]
                            Count -= 1
                        else: # CurrentDigit not in HalfOfDigits
                            if CurrentDigit == Digits[int(Base)]:
                                FractionList[Element[0]] = '0'
                                IndexOfFollowingDigit = Digits.index(FractionList[(Element[0] + 1)])
                                FractionList[(Element[0] + 1)] = Digits[(IndexOfFollowingDigit + 1)]
                                CurrentDigit = FractionList[(Element[0] + 1)]
                                Count -= 1
                            else:
                                IndexOfFollowingDigit = Digits.index(FractionList[(Element[0] + 1)])
                                FractionList[(Element[0] + 1)] = Digits[(IndexOfFollowingDigit + 1)]
                                CurrentDigit = FractionList[(Element[0] + 1)]
                                Count -= 1
            if CurrentDigit == Digits[int(Base)]:
                CurrentDigit = Digits[(int(Base) - 1)]
            FractionList.reverse()
            FractionList = FractionList[:(int(Place) - 1)]
            FractionList.append(CurrentDigit)
            Fraction = ''
            for Element in FractionList:
                Fraction = f'{Fraction}{Element}'
            Radix = f'{Whole}.{Fraction}'
    return Radix


if __name__ == '__main__':
    import builtins
    # Programmer's module/s:
    from BaseNIntegerToBaseTenInteger import BaseNIntegerToBaseTenInteger
    class I():
        RoundRadix = RoundRadix
        BaseNIntegerToBaseTenInteger = BaseNIntegerToBaseTenInteger
    builtins.I = I
    Radix = input('Enter Radix: ')
    Base = input('Enter Base: ')
    Place = input('Enter Place: ')
    Radix = I.RoundRadix(Radix, Base, Place)
    print(Radix)

'''if FractionList[(Element[0] + 1)] == Digits[int(Base)] or FractionList[(Element[0] + 1)] == Digits[(int(Base) - 1)]:
    FractionList[(Element[0]) + 1] = '0'
    IndexOfSecondFollowingDigit = UsedDigits.index(FractionList[(Element[0] + 2)])
    FractionList[(Element[0] + 2)] = UsedDigits[(IndexOfSecondFollowingDigit + 1)]
    CurrentDigit = FractionList[(Element[0] + 1)]
    Count -= 1'''
