def substitution(file):
    # https://www.101computing.net/frequency-analysis/ used for reference

    with open(file, 'r') as f:
        ciphertext = f.read()
    print("ciphertext: ", ciphertext)
    freq = {} 

    for letter in ciphertext:
        if letter not in freq and letter.isalpha():
            freq[letter] = 1
        elif letter.isalpha():
            freq[letter] += 1
    sort = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    total = 0
    for val in sort.values():
        total += val

    percentages = {}
    for key, val in sort.items():
        percentages[key] = (val/total)*100
    
    print("frequencies: ", percentages)

    print("\n\n\n")
    plaintext = ""
    for letter in ciphertext:
        if letter == 'Q':
            letter = 'e'
            plaintext += letter
        elif letter == 'J':
            letter = 't'
            plaintext += letter
        elif letter == 'C':
            letter = 'a'
            plaintext += letter
        elif letter == 'W':
            letter = 'o'
            plaintext += letter
        elif letter == 'Y':
            letter = 'r'
            plaintext += letter
        elif letter == 'U':
            letter = 'b'
            plaintext += letter
        elif letter == 'B':
            letter = 'c'
            plaintext += letter
        # october deciphered, now just finding the closest letter frequency from website to the frequency of the letter
        elif letter == 'E':
            letter = 'v'
            plaintext += letter
        elif letter == 'M':
            letter = 'i'
            plaintext += letter
        elif letter == 'G':
            letter = 'd'
            plaintext += letter
        # don't deciphered -- wow once the ball gets rolling it's easy
        elif letter == 'K':
            letter = 'n'
            plaintext += letter
        elif letter == 'P':
            letter = 'g'
            plaintext += letter
        elif letter == 'I':
            letter = 's'
            plaintext += letter
        #practice deciphered
        elif letter == 'O':
            letter = 'p'
            plaintext += letter
        #a good amount of words are already deciphered now, so i'm pivoting from looking at the frequencies on the website to just making the words make sense now 
        elif letter == 'S':
            letter = 'm'
            plaintext += letter
        elif letter == 'Z':
            letter = 'l'
            plaintext += letter
        elif letter == 'H':
            letter = 'h'
            plaintext += letter
        elif letter == 'N':
            letter = 'u'
            plaintext += letter
        elif letter == 'X':
            letter = 'w'
            plaintext += letter
        elif letter == 'T':
            plaintext += 'y'
        elif letter == 'D':
            plaintext += 'k'
        elif letter == 'R':
            plaintext += 'f'
        else: 
            plaintext += letter
    print("plaintext: ", plaintext)


substitution('challenge2/challenge2.txt')