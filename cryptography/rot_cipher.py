import argparse
def encrypt(text, rot_val):
    enc_wrd = ''
    text = str(text)
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            enc_wrd = enc_wrd + str(chr((ord(char) + int(rot_val)-65) % 26 + 65))
        elif char == " ":
            enc_wrd = enc_wrd + " "
        elif (char.islower()):
            enc_wrd = enc_wrd + str(chr((ord(char) + int(rot_val)-97) % 26 + 97))
        else:
            enc_wrd = enc_wrd + char
    return enc_wrd

def decrypt(text, rot_val):
    dec_wrd = ''
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            dec_wrd = dec_wrd + chr((int(ord(char)) - int(rot_val)-65) % 26 + 65)
        elif char == " ":
            dec_wrd = dec_wrd + " "
        elif (char.islower()):
            dec_wrd = dec_wrd + chr((int(ord(char)) - int(rot_val)-97) % 26 + 97)
        else:
            dec_wrd = dec_wrd + char
    return dec_wrd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', help="True/False")
    parser.add_argument("-d", "--decrypt", help="True/False")
    args = parser.parse_args()
    
    if args.encrypt:
        plaintext = input("Plain text to encrypt: ")
        rot_val = input("ROT Value: ")
        encrypted_wrd = encrypt(plaintext, rot_val)
        print("Encrypted message: " + encrypted_wrd)
    if args.decrypt:
        rot_val = input("ROT Value: ")
        encrypted_wrd = input("Encrypted text to decrypt: ")
        if "all" in rot_val:
            from detectEnglish import *
            potential_keys = []
            for i in range(1, 25):
                decrypted_wrd = decrypt(encrypted_wrd, i)
                if isEnglish(decrypted_wrd):
                    potential_keys.append(i)
            print("\nPotential keys:-\n")
            for i in potential_keys:
                print(f"KEY{i}")
            print("\nShowing results for all potential keys...\n")
            for i in potential_keys:
                decrypted_word = decrypt(encrypted_wrd, i)
                print(f"KEY{i} Decrypted text: {decrypted_word}")
        else:
            decrypted_wrd = decrypt(encrypted_wrd, rot_val)
            print("Decrypted message: " + decrypted_wrd)        
