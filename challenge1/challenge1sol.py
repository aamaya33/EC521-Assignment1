# 4 different types of cyphers
# 1. Casear Cypher -- shift the letters by a fixed number
def caesar_cypher(file):
    with open(file, 'r') as f:
        ciphertext = f.read()

    ciphertext = "^s<qN}{;t~bp?vN}{;"
    for shift_len in range(128):
        decrypted = ""
        for ch in ciphertext:
            decrypted += chr((ord(ch)-shift_len)%128)
        print(f"Shift len = {shift_len}: {decrypted}")  

caesar_cypher('challenge1.txt')
            