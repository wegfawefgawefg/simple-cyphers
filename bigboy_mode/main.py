"""assymetric encryption
msg = "gibson is a nerd, and my mom is fat"

encode(private_key, msg) -> encoded msg
decode(public_key, encoded_msg) -> decoded msg
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from pprint import pprint

pubkey = "12345"
privkey = "12345"

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
msg = "potato"
encoded_msg = private_key.sign(msg)
print(encoded_msg)
# print(private_key)
# pprint(dir(private_key))
# print(private_key.private_numbers())
# print(private_key.private_bytes())

# print(private_key.public_key().private_numbers())
