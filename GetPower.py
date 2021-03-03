# Python 3.9.0

# GetPower

def GetPower(Root, Exponent):

    
    '''
    Parameter requirements:
    Root: must be a literal integer or float.
    Exponent: must be a literal integer.
    '''

    
    Power = Root
    for Times in range(Exponent - 1):
        Power *= Root
    return Power


if __name__ == '__main__':
    import builtins
    class I():
        GetPower = GetPower
    builtins.I = I
    Root = float(input('Enter Root: '))
    Exponent = int(input('Enter Exponent: '))
    Power = I.GetPower(Root, Exponent)
    print(Power)
