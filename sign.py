from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

def sign(m):
    #generate public key
    private_key, public_key = gen_keypair(secp256k1)

    #generate signature
    r, s = ecdsa.sign(m, private_key)
    #print("verify:", ecdsa.verify((r, s), m, public_key))
    return( public_key, [r, s] )


