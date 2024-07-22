enc = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16] # a - p

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def b16_decode(encoded):
	plain = ""
	for i in range(0, len(encoded) - 1, 2):
		j = i + 1
		bin1 = "{0:04b}".format(ALPHABET.find(encoded[i]))
		bin2 = "{0:04b}".format(ALPHABET.find(encoded[j]))
		plain += chr(int(bin1 + bin2, 2))

	return plain

for key in ALPHABET:
	out = ""
	for _, c in enumerate(enc):
		out += shift(c, key)

	print("picoCTF{" + b16_decode(out) + "}")