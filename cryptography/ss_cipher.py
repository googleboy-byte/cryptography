# SIMPLE SUBSTITUTION CIPHER ENCRYPTOR/DECRYPTOR

import random
import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def createRandKey():
    key = list(ALPHABET)
    random.shuffle(key)
    return "".join(key)

def isKeyValid(key):
    key = list(key)
    key.sort()
    letters =  list(ALPHABET)
    if key != letters:
        sys.exit("There is something wrong with the key")
    else:
        return True

def trnslt(txt, mode, key):
    A = ALPHABET
    B = key
    translated = ''
    if 'd' in mode:
        A, B = B, A
    for i in txt:
        if i.upper() in A:
            index = A.find(i.upper())
            if i.isupper():
                translated = translated + B[index].upper()
            elif i.islower():
                translated = translated + B[index].lower()
            elif i == " ":
                translated = translated + " "
        else:
            translated = translated + i
    return translated

def encrypt(txt):
    key = createRandKey()
    isKeyValid(key)    
    return trnslt(txt, 'e', key), key

def decrypt(key, txt):
    return trnslt(txt, 'd', key)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', help="True/False")
    parser.add_argument("-d", "--decrypt", help="True/False")
    args = parser.parse_args()
    
    if args.encrypt:
        ptext = input("Plain text to encrypt: ")
        etext, key = encrypt(ptext)
        print(f"\nUsing key: {key}\n")
        print(f"Encrypted text: {etext}")
    elif args.decrypt:
        etext = input("Encrypted text to decrypt: ")
        key = input("Key: ")
        print(f"\nDecrypted text: {decrypt(key, etext)}")    

if __name__ == "__main__":
    main()