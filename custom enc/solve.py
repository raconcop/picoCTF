from sympy import mod_inverse

# Dynamic XOR decryption function
def dynamic_xor_decrypt(cipher_text, text_key):
    decrypted_text = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted_text += decrypted_char
    return decrypted_text

# Reverse the modular exponentiation to obtain the original ciphertext
def reverse_generator(g, x, p):
    return pow(g, x, p)

# Decrypt function to reverse the encryption process
def decrypt(cipher, key):
    decrypted_text = ""
    for num in cipher:
        decrypted_num = num // (key*311)  # Reversing the encryption operation
        decrypted_text += chr(decrypted_num)
    return decrypted_text

# Constants from the provided information
a = 94
b = 29
enc_flag = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]

p = 97
g = 31

# Reverse modular exponentiation to obtain shared key
u = reverse_generator(g, a, p)
v = reverse_generator(g, b, p)
shared_key = reverse_generator(v, a, p)

# Decrypt intermediate ciphertext
intermediate_ciphertext = decrypt(enc_flag, shared_key)

# Reverse dynamic XOR encryption
flag = dynamic_xor_decrypt(intermediate_ciphertext, "trudeau")

print("Decoded Flag:", flag[::-1])