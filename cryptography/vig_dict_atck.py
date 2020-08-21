import detectEnglish
import vigenere_cipher

etext = input("Encrypted text to decode: ")

def bruteVigKey(etxt):
    f = open('dictionary.txt')
    wrds = f.readlines()
    f.close()
    for i in wrds:
        wrd = i.strip()
        ptext = vigenere_cipher.decrypt(wrd, etxt)
        if detectEnglish.isEnglish(ptext, wordPercentage=40):
            print(f"\nPossible decrypted text: {ptext}")
            willcontinue = input("Enter T to terminate brute attack or just press Enter to continue: ")
            if 'T' in willcontinue.upper():
                return ptext
            else:
                pass

if __name__ == "__main__":
    bruteVigKey(etext)
                