UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionary = open('dictionary.txt')
    Words = {}
    for i in dictionary.read().split('\n'):
        Words[i] = None
        dictionary.close()
    return Words

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches = matches + 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return "".join(lettersOnly)

def isEnglish(message, wordPercentage=10, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch