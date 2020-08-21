ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def crypt(key, txt, cryptmode):
    crypted = []
    key = key.upper()
    indx = 0
    for i in txt:
        char_check = ALPHABET.find(i.upper())
        if char_check != -1:
            if cryptmode == "decrypt":
                char_check = char_check - ALPHABET.find(key[indx])
            elif cryptmode == "encrypt":
                char_check = char_check + ALPHABET.find(key[indx])
            char_check %= len(ALPHABET)
            if i.isupper():
                crypted.append(ALPHABET[char_check])
            elif i.islower():
                crypted.append(ALPHABET[char_check].lower())
            indx = indx + 1
            if indx == len(key):
                indx = 0
        else:
            crypted.append(i)
    return "".join(crypted)

def encrypt(key, txt):
    print(f"Encrypted text: " + crypt(key, txt, 'encrypt'))

def decrypt(key, txt):
    return crypt(key, txt, 'decrypt')

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', help="True/False")
    parser.add_argument("-d", "--decrypt", help="True/False")
    args = parser.parse_args()   
    key = input("Key for vigenere cipher: ")     
    if args.encrypt:
        plaintext = input("Plaintext to encrypt: ")
        encrypt(key, plaintext)
    elif args.decrypt:
        etext = input("Encrypted text to decrypt: ")
        print(f"Decrypted text: {decrypt(key, etext)}")
       

if __name__ == "__main__":
    main()