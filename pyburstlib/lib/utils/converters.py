'''
pyburstlib
:author: drownedcoast
:date: 3-18-2018
'''
import binascii
import codecs
import string

def int_from_bytearray(ba):
    # byteorder must be little
    return int.from_bytes(ba, byteorder='little', signed=False)

def string_to_hex_string(message):
    return message.encode('utf-8').hex()

def hex_string_to_bytes(message):
    if is_hex(message):
        return codecs.decode(message, 'hex_codec')
    return bytes()

def hex_string_to_byte_array(message):
    if is_hex(message):
        return bytearray.fromhex(message)
    return bytearray()

def bytearray_to_hex_string(message):
    return message.hex()

def is_hex(message):
    if type(message) == str and len(message) > 0:
        hex_digits = set(string.hexdigits)
        return all(d in hex_digits for d in message)
    return False