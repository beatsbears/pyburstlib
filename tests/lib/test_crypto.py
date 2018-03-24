'''
pyburstlib
:author: drownedcoast
:date: 3-18-2018
'''
import pyburstlib.lib.crypto as crypto

PASSWORD1 = 'testpass'
PUBKEY1 = '5e7c74732edd765a948d6a070f2dc61dc140f5b3c8c6b36ca44e54e83a5b1954'
ACCOUNTID1 = 17836903925142865226
ADDRESS1 = 'BURST-LKCC-MQRG-7NH6-HBD4H'

class TestCrypto:
    '''
    Unit tests for crypto module
    '''
    def test_public_key_from_password1(self):
        assert crypto.get_public_key(PASSWORD1) == PUBKEY1, \
        'Expected {} to generate public key {}'.format(PASSWORD1, PUBKEY1)

    def test_account_id_from_password(self):
        account_id = crypto.get_account_id(PASSWORD1)
        assert account_id == ACCOUNTID1, \
        'Expected {} to generate account id {}'.format(PASSWORD1, ACCOUNTID1)
        assert type(account_id) == int, \
        'Expected return type to be int'
        assert 20 >= len(str(account_id)) >=19, \
        'Expected account id to be 19 or 20 digits long'

    