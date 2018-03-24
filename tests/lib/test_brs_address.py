'''
pyburstlib
:author: drownedcoast
:date: 3-24-2018
'''
import pyburstlib.lib.brs_address as brs

ACCOUNTID1 = 17836903925142865226
ADDRESS1 = 'BURST-LKCC-MQRG-7NH6-HBD4H'

ACCOUNTID2 = 8435526664171750194
ADDRESS2 = 'BURST-Q2TL-TV5N-D5QK-94A6C'

BAD_ACCOUNTID = 27836903925142865226

class TestBRSAddress:
    '''
    Unit tests for brs_address module
    '''
    def test_to_string_empty(self):
        addr = brs.BRSAddress()
        assert addr.to_string() == 'BURST-2223-2222-2222-22222'
        assert addr.codeword == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def test_to_string(self):
        addr = brs.BRSAddress()
        addr.set_address(ACCOUNTID1)
        assert ACCOUNTID1 != ACCOUNTID2
        assert addr.to_string() == ADDRESS1
        addr.set_address(str(ACCOUNTID1))
        assert addr.to_string() == ADDRESS1
        addr.set_address(ACCOUNTID2)
        assert addr.to_string() == ADDRESS2
        addr.set_address(str(ACCOUNTID2))
        assert addr.to_string() == ADDRESS2
    
    def test_set_address_invalid(self):
        addr = brs.BRSAddress()
        assert addr.set_address(BAD_ACCOUNTID) == False
        assert addr.set_address(str(ACCOUNTID1)[0:17]) == False

    def test_set_address(self):
        addr = brs.BRSAddress()
        assert addr.set_address(ACCOUNTID1) == True
        assert addr.set_address(ACCOUNTID2) == True

