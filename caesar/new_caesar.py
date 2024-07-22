import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16] # a - p



## for each letter we encode it to binary
## then we shift it based on the key

# B16 
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		print(binary) # 01100001
		enc += ALPHABET[int(binary[:4], 2)] # 0110 : g
		enc += ALPHABET[int(binary[4:], 2)] # 0001 : b
	return enc




# Caesar shift
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "ab"
key = "a"
assert all([k in ALPHABET for k in key]) # a - p
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)





