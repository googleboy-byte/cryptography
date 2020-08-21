import math
from detectEnglish import *

def encrypt(key, ptext):
    
    enc_text = [""] * key
    for i in range(key):
        current_letter = i
        while current_letter < len(ptext):
            enc_text[i] += ptext[current_letter]
            current_letter += key
    return "".join(enc_text)

def decrypt(key, etext):
    cols = math.ceil(len(etext) / int(key))
    rows = int(key)
    unfilled_boxes = (cols * rows) - len(etext)
    ptext = [""] * cols
    col = 0
    row = 0
    for i in etext:
        ptext[col] = ptext[col] + i
        col = col + 1
        if (col == cols) or (col == cols - 1 and row > rows - unfilled_boxes):
            col = 0
            row = row + 1
    return "".join(ptext)

def bruteKey(etext):
    print("\nTrying to bruteforce transposition key...")
    potential_keys = []
    for i in range(1, len(etext)):
        decrypted_text = decrypt(i, etext)
        if isEnglish(decrypted_text):
            potential_keys.append(i)
    return potential_keys

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', help="True/False")
    parser.add_argument("-d", "--decrypt", help="True/False")
    args = parser.parse_args()    
    
    if args.encrypt:
        plaintext = input("Plain text to encrypt: ")
        cols = input("Key: ")
        cols = int(cols)        
        print(f"Encrypted text: {encrypt(cols, plaintext)}")
    elif args.decrypt:
        encryptedtext = input("Encrypted text to decrypt: ")
        cols = input("Key: ")
        if 'all' in cols:
            potential_keys = bruteKey(encryptedtext)
            print("\nPotential Keys :-\n")
            for i in potential_keys:
                print(f"Key: {i}")
            print("\nShowing result for each potential key")
            for i in potential_keys:
                print(f"\nKey{i} Decrypted text: {decrypt(i, encryptedtext)}")
        else:
            cols = int(cols)
            print(f"Decrypted text: {decrypt(cols, encryptedtext)}")    

if __name__ == "__main__":
    main()