# Python 3.9.0

# Radix

def Radix(Radix):


    '''
    Parameters:
    Radix: must be a string radix ('n', 'n.n')
    '''


    if '.' not in Radix:
        Radix = f'{Radix}.0'
    return Radix


if __name__ == '__main__':
    import builtins
    class I():
        Radix = Radix
    builtins.I = I
    Radix = input('Enter Radix: ')
    Radix = I.Radix(Radix)
    print(Radix)
