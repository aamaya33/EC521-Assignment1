header = bytes([0x50, 0x4B, 0x03, 0x04, 0x0A, 0x00]) # first 6 bytes of valid zip file header

with open('challenge3', 'rb') as f:
	data = f.read()

key = bytes([data[i] ^ header[i] for i in range(6)]) # xor with the header to get the key
print(key)
file_content = bytes([data[i] ^ key[i % 6] for i in range(len(data))]) 

with open('challenge3.zip', 'wb') as f:
	f.write(header + key + file_content)

