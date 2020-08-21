import os, re, copy, pprint, pyperclip, ss_cipher, makeWordPatterns

if not os.path.exists('wordPatterns.py'):
    makeWordPatterns.main() # create the wordPatterns.py file
import wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    message = input("Encrypted text: ")

    print('Hacking...')
    letterMapping = hackSimpleSub(message)
    print('Mapping:')
    pprint.pprint(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    print(hackedMessage)


def getBlankCipherletterMapping():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):

    letterMapping = copy.deepcopy(letterMapping)
    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])
    return letterMapping


def intersectMappings(mapA, mapB):
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
   
    letterMapping = copy.deepcopy(letterMapping)
    loopAgain = True
    while loopAgain:
        loopAgain = False
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        
        newMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getPattern(cipherword)
        if wordPattern not in wordPatterns.patterns:
            continue
        for candidate in wordPatterns.patterns[wordPattern]:
            newMap = addLettersToMapping(newMap, cipherword, candidate)

        intersectedMap = intersectMappings(intersectedMap, newMap)

    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    return ss_cipher.decrypt(key, ciphertext)


if __name__ == '__main__':
    main()

