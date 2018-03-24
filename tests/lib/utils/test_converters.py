'''
pyburstlib
:author: drownedcoast
:date: 3-21-2018
'''
from pyburstlib.lib.utils import converters

class TestConverters:
    '''
    Unit tests for converters
    ''' 
    def test_int_from_bytearay(self):
        ba1 = bytearray.fromhex('ae423a')
        assert converters.int_from_bytearray(ba1) == 3818158
        assert type(converters.int_from_bytearray(ba1)) is int

    def test_string_to_hex_string(self):
        assert converters.string_to_hex_string('testpass') == '7465737470617373'
        assert type(converters.string_to_hex_string('testpass')) is str
        assert converters.is_hex(converters.string_to_hex_string('testpass')) is True

    def test_hex_string_to_bytes(self):
        assert converters.hex_string_to_bytes('7465737470617373') == b'testpass'
        assert type(converters.hex_string_to_bytes('7465737470617373')) is bytes
        assert converters.hex_string_to_bytes('zzzz1234567890') == b'', \
            'Expected empty bytes to be returned for non-hex input'
    
    def test_hex_string_to_byte_array(self):
        assert converters.hex_string_to_byte_array('7465737470617373') == bytearray(b'testpass')
        assert type(converters.hex_string_to_byte_array('7465737470617373')) is bytearray
        assert converters.hex_string_to_byte_array('zzzz1234567890') == bytearray(b''), \
            'Expected empty bytearray to be returned for non-hex input'

    def test_bytearray_to_hex_string(self):
        assert converters.bytearray_to_hex_string(bytearray(b'testpass')) == '7465737470617373'
        assert type(converters.bytearray_to_hex_string(bytearray(b'testpass'))) is str
        assert converters.is_hex(converters.bytearray_to_hex_string(bytearray(b'testpass'))) is True

    def test_is_hex(self):
        assert converters.is_hex('1234') is True
        assert converters.is_hex('zzzz') is False
        assert converters.is_hex(True) is False
        assert converters.is_hex('') is False
        assert converters.is_hex(1234) is False
    
