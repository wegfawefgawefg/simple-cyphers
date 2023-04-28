import sys


def encode(msg):
    encoded_characters = []
    for char in msg:
        encoded_char = chr(ord(char) + 1)
        encoded_characters.append(encoded_char)

    encoded_msg = "".join(encoded_characters)
    return encoded_msg


for line in sys.stdin:
    print(encode(line), end="")
