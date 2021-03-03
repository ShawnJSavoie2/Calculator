# Python 3.9.0

# Common

def Common(Common):

    
    '''
    Parameter requirements:
    Common: must be a string common ('n', 'n|n' or 'n:n|n').
    '''

    
    if ':' not in Common and '|' not in Common:
        Common = f'{Common}:0|0'
    if ':' not in Common and '|' in Common:
        Common = f'0:{Common}'
    return Common


if __name__ == '__main__':
    import builtins
    class I():
        Common = Common
    builtins.I = I
    Common = input('Enter Common: ')
    Common = I.Common(Common)
    print(Common)
    
