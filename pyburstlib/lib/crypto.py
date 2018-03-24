'''
pyburstlib
:author: drownedcoast
:date: 3-18-2018
'''
from hashlib import sha256
import nacl.public as curve25519 #pynacl

import pyburstlib.lib.utils.converters as conv

def get_public_key(secret_pass):
    # 1. hex string to bytes
    # 2. sha256 as bytes
    # 3. curve25519 keygen .p (?) 
    # 4. byte array to hex string
    secret_pass_as_hex = secret_pass
    if not conv.is_hex(secret_pass):
        secret_pass_as_hex = conv.string_to_hex_string(secret_pass)
    b = conv.hex_string_to_bytes(secret_pass_as_hex)
    bh = simple_hash(b)
    pub = curve25519.PrivateKey(bh).public_key._public_key # as bytes
    return conv.bytearray_to_hex_string(pub)

def get_account_id(secret_pass):
    # 1. secret pass to hex stirng
    # 2. public key from hex string
    # 3. hex string to bytes
    # 4. sha256 as bytes
    # 5. bytes to hex string
    # 6. hex string to byte array
    # 7. slice 0,8 from array
    # 8. byte array to big int to str
    hex_pass = secret_pass
    if not conv.is_hex(secret_pass):
        hex_pass = conv.string_to_hex_string(secret_pass)
    pub_key = get_public_key(hex_pass)
    pub_key_as_bytes = conv.hex_string_to_bytes(pub_key)
    sha_hash = simple_hash(pub_key_as_bytes)
    hex_str = conv.bytearray_to_hex_string(sha_hash)
    byte_array = conv.hex_string_to_byte_array(hex_str)
    return conv.int_from_bytearray(byte_array[:8])

def get_account_address(secret_pass):
    return ''

def simple_hash(message):
    h = sha256()
    h.update(message)
    return h.digest()

def curve25519_pub_from_seed(seed):
    return curve25519.PrivateKey(seed).public_key

