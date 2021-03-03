# Python 3.9.0

# GetExponent

def GetExponent(Root, Power):

    
    '''
    Parameter requirements:
    Power: must be a literal integer or float.
    Root: must be a literal integer or float.
    '''

    
    Exponent = 1
    while Power != Root:
        Power = Power / Root
        Exponent += 1
    return Exponent


if __name__ == '__main__':
    import builtins
    class I():
        GetExponent = GetExponent
    builtins.I = I
    Power = float(input('Enter Root: '))
    Root = float(input('Enter Power: '))
    Exponent = I.GetExponent(Power, Root)
    print(Exponent)
