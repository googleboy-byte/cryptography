def encrypt(msg):
    encrypted = ''
    ltr_count = len(msg) - 1
    while ltr_count >= 0:
        encrypted =  encrypted + msg[ltr_count]
        ltr_count = ltr_count - 1
    return encrypted

def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt')
    parser.add_argument("-d", "--decrypt")
    args = parser.parse_args()
    
    if args.encrypt:
        plaintext = input("Plain text to encrypt: ")
        encrypted_wrd = encrypt(plaintext)
        print("Encrypted message: " + encrypted_wrd)
    if args.decrypt:
        encrypted_wrd = input("Encrypted text to decrypt: ")
        decrypted_wrd = encrypt(encrypted_wrd)
        print("Decrypted message: " + decrypted_wrd)    

if __name__ == "__main__":
    main()