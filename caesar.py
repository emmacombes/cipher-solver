from util import get_input, get_int_input, char_to_int, int_to_char
from errors import InvalidCharError


def decode_caesar(ciphertext, offset):
    """
     TODO: this function should return the plaintext. For example:

     "SGHR HR Z SDRS." should return "THIS IS A TEST." (note that punctuation
     is preserved)
    """
    output = ''

    for char in ciphertext:
        try:
            integer = char_to_int(char)
            integer += offset
            integer = integer % 26
            char = int_to_char(integer)
            output += char
        except InvalidCharError:
            output += char
    return output


def solve_caesar(ciphertext):
    """ TODO: this function should solve the caesar cipher automatically.

    There are lots of ways to do this and you can do it whatever way you like,
    as long as it is accurate.

    Here is one way: the distribution of letters in the English langauge is
    far from uniform. Since there are only 26 possibilities you can simply try
    each one and score it using a function that determines how close the
    current distribution of letters is to English (yay stats).
    """
    return (ciphertext, offset)



# The __name__ global variable holds the name of the current python file as it
# was imported. E.g. let's say I have a python package called stripe and in the
# main file I have 'from .errors import X'. If the code inside the errors file
# looked at __name__ it would hold 'stripe.errors'.
#
# The only exception to this is when the current file wasn't imported it was
# ran directly (e.g. typing python [filename] into the terminal). In this case
# it holds the value '__main__'.
#
# So why do we use this? Suppose we wanted to write an affine cipher solver
# (you don't need to know what this is) and wanted to reuse some of the
# functions from here. If we didn't do this then when the affine.py file
# imported them it would suddenly start asking the user for input. This way,
# it only asks the user for input if this is the file that is actually being
# run.

if __name__ == '__main__':
    # Get the ciphertext
    ciphertext = get_input()

    # Get the offset to try
    offset = get_int_input()

    print decode_caesar(ciphertext, offset)
