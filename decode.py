import sys


def decode(msg):
    decoded_characters = []
    for char in msg:
        decoded_char = chr(ord(char) - 1)
        decoded_characters.append(decoded_char)

    decoded_msg = "".join(decoded_characters)
    return decoded_msg


for line in sys.stdin:
    print(decode(line), end="")
