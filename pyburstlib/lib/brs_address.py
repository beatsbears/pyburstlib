'''
pyburstlib
:author: drownedcoast
:date: 3-24-2018
'''

class BRSAddress:
    '''
    Creates a Burst address from an account Id
    '''
    codeword = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    syndrome = [0, 0, 0, 0, 0]
    gexp = [1, 2, 4, 8, 16, 5, 10, 20, 13, 26, 17, 7, 14, 28, 29, 31, 27, 19, 3, 6, 12, 24, 21, 15, 30, 25, 23, 11, 22, 9, 18, 1]
    glog = [0, 0, 1, 18, 2, 5, 19, 11, 3, 29, 6, 27, 20, 8, 12, 23, 4, 10, 30, 17, 7, 22, 28, 26, 21, 25, 9, 16, 13, 14, 24, 15]
    cwmap = [3, 2, 1, 0, 7, 6, 5, 4, 13, 14, 15, 16, 12, 8, 9, 10, 11]
    alphabet = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ'
    guess = []

    def __init__(self):
        self.address = None

    def to_string(self):
        '''
        Returns the 'BURST-xxxx-xxxx-xxxx-xxxxx' address for the BRSAddress object.
        '''
        out = 'BURST-'
        for i in range(17):
            out += self.alphabet[self.codeword[self.cwmap[i]]]
            if i & 3 == 3 and i < 13:
                 out += '-'
        self.address = out
        return self.address
    
    def set_address(self, account_id):
        '''
        Seeds the account id for a Burst address.
        Currently only supports generating address from account ids
        '''
        # length = 0
        # self.guess = []
        self.reset()
        if not type(account_id) == str:
            account_id = str(account_id)
        if 19 <= len(account_id) <= 20 and account_id.isdigit():
            return self.from_acct(account_id)
        return False

    def from_acct(self, account_id):
        '''
        Creates the codeword used to generate a 'BURST-xxxx-xxxx-xxxx-xxxxx' from an account id.
        '''
        inp = [0] * len(account_id)
        out = []
        pos = 0
        length = len(account_id)

        if (length == 20 and account_id[0] != '1'):
            return False
        for i in range(length):
            inp[i] = ord(account_id[i]) - ord('0')
        while True:
            divide = 0
            newlen = 0

            for i in range(length):
                divide = divide * 10 + inp[i]
                if divide >= 32:
                    inp[newlen] = divide >> 5
                    newlen += 1
                    divide = divide & 31
                elif newlen > 0:
                    inp[newlen] = 0
                    newlen += 1
            
            length = newlen
            if len(out) > pos:
                out[pos] = divide
            else:
                pos += 1
                out.append(divide)
            if not newlen:
                break

        for i in range(13):
            if (pos) >= 0:
                self.codeword[i] = out[i]
            else:
                self.codeword[i] = 0
            pos -= 1
        self.encode()
        return True
        

    def encode(self):
        p = [0, 0, 0, 0]
        for i in range(12, -1, -1):
            fb = self.codeword[i] ^ p[3]
            p[3] = p[2] ^ self.gmult(30, fb)
            p[2] = p[1] ^ self.gmult(6, fb)
            p[1] = p[0] ^ self.gmult(9, fb)
            p[0] = self.gmult(17, fb)
        self.codeword[13] = p[0]
        self.codeword[14] = p[1]
        self.codeword[15] = p[2]
        self.codeword[16] = p[3]
    
    def gmult(self, a, b):
        if a == 0 or b == 0:
            return 0
            
        idx = (self.glog[a] + self.glog[b]) % 31
        return self.gexp[idx]

    def reset(self):
        for i in range(17):
            self.codeword[i] = 1

