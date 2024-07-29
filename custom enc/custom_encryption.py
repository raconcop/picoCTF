from random import randint
import sys

# Generate alg

# G to the power of X mod P
def generator(g, x, p):
    return pow(g, x) % p

# Encryption alg
# cipher variable is created then each letter is converted to an int with ord, multiplied by key and 311
def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        # numerical version of the char
        cipher.append(((ord(char) * key*311)))
    return cipher
# returns an array with a bunch of numbers 





# Checks for prime 
def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True
# Returns true or false based on if its a prime number    
    

# Xor encrypt
# takes in a string and string key
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key) # length of the key
    for i, char in enumerate(plaintext[::-1]): # for i, each char var 
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text
# Returns a string
# No randomness always the same result


# Some form of a one way enc alg
# Tests for the enc

def test(plain_text, text_key):
    p = 94
    g = 29
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return

    
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    print('semi cip xor encrypted: ', semi_cipher)
    
    
    
    
    print('shared key: ',shared_key)

    # encrypt takes a string and an int
    # takes in a xor encrypted ciphertext and scrambles with a shared key
    cipher = encrypt(semi_cipher, shared_key)

    print(cipher)


if __name__ == "__main__":
    message = "picoCTF"
    test(message, "trudeau")
