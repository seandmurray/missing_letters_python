import string

global LETTER_MAP

def initLetterMap ():
    letterMap = {}
    allLettersLowerCase = list(string.ascii_lowercase)
    while len(allLettersLowerCase) > 0:
        letter = list.pop(allLettersLowerCase)
        letterMap[letter] = letter;
    return letterMap

def processLine (line):
    letterMap = LETTER_MAP.copy()
    for letter in list(line.lower()):
        if letter in letterMap:
           del letterMap[letter] 
    leftovers = list(letterMap.keys())
    leftovers.sort()
    return ''.join(leftovers)

def closefp (fp):
    try:
        fp.close()
    except:
        noop

def processFile (filepath):
    try:
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                print(processLine(line))
                line = fp.readline()
        closefp(fp)
    except:
        print("Was unable to process file: " + filepath)

LETTER_MAP = initLetterMap();
ALL_LETTERS_USED = 'All letters in the english alphabet have been used.'
