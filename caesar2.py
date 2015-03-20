from caesar import decode_caesar
from util import get_input

if __name__ == '__main__':
    # Get the ciphertext
    ciphertext = get_input()

    for offset in range(0,25):
        print decode_caesar(ciphertext, offset)
