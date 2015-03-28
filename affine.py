from util import get_input, get_int_input, char_to_int, int_to_char, invmodp
from errors import InvalidCharError, InvalidInputError

def decode_affine(ciphertext, multiply, offset):
    """
     TODO: this function should return the plaintext. For example:

     "SGHR HR Z SDRS." should return "THIS IS A TEST." (note that punctuation
     is preserved)
    """
    output = ''
    try:
        inverse = invmodp(multiply,26)
    except ValueError:
        raise InvalidInputError('%d has no inverse mod 26' % (multiply))

    for char in ciphertext:
        try:
            integer = char_to_int(char)
            integer = (integer - offset) * inverse
            integer = integer % 26
            char = int_to_char(integer)
            output += char
        except InvalidCharError:
            output += char
    return output



if __name__ == '__main__':
    # Get the ciphertext
    ciphertext = get_input()

    #Get the multiplier
    multiply = get_int_input()

    # Get the offset to try
    offset = get_int_input()

    print decode_affine(ciphertext, multiply, offset)
