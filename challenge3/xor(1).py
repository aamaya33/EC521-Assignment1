plaintext = "EC521VERYSECRETTEXT"

key = "TERRIERS"

ciphertext = ""

for pos in range(len(plaintext)):
	ciphertext += chr(ord(plaintext[pos])^ord(key[pos%len(key)]))

#print(ciphertext)

plaintext2 = ""

for pos in range(len(ciphertext)):
	plaintext2 += chr(ord(ciphertext[pos])^ord(key[pos%len(key)]))

#print(plaintext2)

plain = 'plainheader'
enc = 'header'

with open(plain, 'r') as f:
	plain = f.read()
	
with open(enc, 'r') as f:
	enc = f.read()

recoveredkey = ""

for pos in range(len(enc)):
	recoveredkey += chr(ord(enc[pos])^ord(plain[pos%len(plain)]))

print(recoveredkey)

