from errors import InvalidCharError

def get_input(msg='Enter ciphertext: '):
    """ Get string input from user """
    return raw_input(msg)

def get_int_input(msg='Enter integer: '):
    """ Get integer input from user """
    while(True):
        try:
            value = raw_input(msg)
            value = int(value)
        except ValueError:
            print '"%s" is not a valid integer' % value
            continue
        return value

def char_to_int(char):
    """ This function converts a character into an integer. It raises an
    exception if the character is not in the alphabet (e.g. punctuation)
    """
    char = char.upper() # uppercase letters have different codes than
                        # lowercase letters, so we have to be consistent.
                        # I have chosen to use uppercase
    value = ord(char) - 65
    if -1 < value < 26:
        return value

    raise InvalidCharError("The char '%s' is not in A-Z" % char)


def int_to_char(int):
    return chr(int + 65);
