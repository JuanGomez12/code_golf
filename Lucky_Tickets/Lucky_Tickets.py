import sys

class NumberingEncoder():
  def __init__(self) -> None:
    self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"

    @classmethod
    def encode(self,n):
        try:
            return self.alphabet[n]
        except IndexError:
            raise Exception ("cannot encode: %s" % n)

    @classmethod
    def dec_to_base(sef, dec, base):
        if dec < base:
            return encode (dec)
        else:
            return dec_to_base (dec // base, base) + encode (dec % base)
  
def base_to_dec(num, base):
  pass


for digits, notation in zip(sys.argv[1::2], sys.argv[2::2]):
    digit=digits/2